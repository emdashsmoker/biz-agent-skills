# Acquisition and activation by ecosystem

> This English version is a translation of the Korean original. It may behave differently from what the original intends.

Each section covers how to download files that match the target environment, how to pack them into the payload, how to activate them in the target environment, and where things often break. Commands are examples. Option names can change between tool versions, so when a command fails, check the current options with the tool's --help.

## Python packages

Without conditions, pip picks files for the build environment's Python version and operating system. State the target conditions when downloading.

```
pip download <package> -d wheels --only-binary=:all: \
  --python-version 3.12 --implementation cp \
  --platform manylinux2014_x86_64
```

You can pass --platform several times. The number in a manylinux tag is the minimum glibc version it needs, so leave out tags higher than the target environment's glibc.

For packages that ship only a source distribution without wheels, build wheels ahead of time with `pip wheel <package> -w wheels`. Build on the same Python version and operating system as the target environment. Installing a source distribution offline fails when pip tries to download build tools. A wheel with a compiled C extension works only on glibc at or above the version of the system that built it, so build it on a system whose glibc is the same as or older than the target environment's.

Activate with `pip install --no-index --find-links <wheel folder> <package>`. Where pip is missing or installs are blocked, extract the wheels into the working path and add that path to PYTHONPATH. This works for packages that need no console commands and no post-install steps. A large wheel shrinks when you extract it and repack it as tar.xz, and activation extracts it and uses it through PYTHONPATH.

Common failure points are below.

- (Undeclared dependencies) Some libraries import packages missing from their metadata. After installing, run the parent skill's imports and main calls to find the gaps
- (First-use downloads) Some libraries download tokenizer data, corpora, or model weights on the first call. Run them once in the build environment to fill the cache, put the cache folder in the payload, and point the library's cache path environment variable at it. TIKTOKEN_CACHE_DIR in tiktoken is one example
- (GPU builds by default) Deep learning frameworks sometimes resolve to the GPU build plus several GB of GPU libraries from the default index. For a CPU target, point to the CPU-only index, and check the downloaded file list to confirm the CPU build stays in place while you download further packages
- (Python version) Wheels tagged with a version such as cp312 do not install on other versions. Wheels tagged abi3 work on the tagged version and later. `pip debug --verbose` lists the wheel tags the target environment accepts

## Node.js packages

Packages that carry native binaries pick a sub-package for the operating system and CPU at install time. Install in the build environment with the target conditions stated.

```
npm install <package> --os=linux --cpu=x64 --libc=glibc
```

Some packages download extra binaries or browsers during installation. Pack the node_modules folder as it stands after installation finishes in the build environment. node_modules holds hundreds to thousands of files, so pack it into one tar.xz.

At activation, extract node_modules into the working path. For CommonJS scripts that load packages with require, set NODE_PATH to the node_modules path. ES modules loaded with import ignore NODE_PATH and look for node_modules in the script's folder and its parent folders. If the skill folder is read-only, copy the parent skill's script into the working path and run it next to node_modules.

Packages built for browsers sometimes require functions the browser provides, as global functions. A canvas text-width measuring function is a common example. To use such a package in Node, you must provide that function yourself, and output quality can differ from the browser. WASM packages run on any operating system and CPU, so they serve as an alternative when native binaries cause compatibility problems.

## Executables

From the official release assets, pick the file that matches the target environment's operating system and architecture. File naming rules differ by project, so pick from the asset list in the release API or on the release page.

If releases are unreachable, consider building from source. Read the repository's build settings, CI settings, and developer documents, and follow the method current at that time. Build only the executable targets you need. Repository size and build time can reach GB and tens of minutes, so check free disk space first. If the repository pins a toolchain version, the build environment must be able to download that version.

A dynamically linked executable does not run on glibc older than that of the system that built it. Read the required version with the command below and compare it with the target environment's glibc.

```
objdump -T <executable> | grep -o 'GLIBC_[0-9.]*' | sort -Vu | tail -1
```

If the target environment's glibc is unknown, pick a statically linked build or an official build made on old glibc.

Strip debug information from executables with strip, then compress them with xz before packing. At activation, extract them into the working path, set the execute permission, and add them to PATH. Point LD_LIBRARY_PATH at any shared libraries they need.

Young tools change command names and options between versions. After activation, read the current command set with `--help` and compare it with how the parent skill calls the tool. If a name changed, find the command with the same function and connect it to the parent skill.

## Java

Collect JAR libraries together with their transitive dependencies from repositories such as Maven Central. If the build environment has Maven, `mvn dependency:copy-dependencies` collects them in one step. The claude.ai package manager allow list has no Maven repository, so Java libraries often need a dependency skill.

Compile Java code written for the parent skill with `javac --release <version>` to match the target environment's runtime version, and bundle the compiled classes. A minimal runtime has no compiler, so it cannot run source files directly.

If the target environment has no Java, bundle a runtime as well.

- Find the needed modules with `jdeps --print-module-deps --ignore-missing-deps <JAR list>`
- Build a minimal runtime with `jlink --add-modules <module list> --strip-debug --no-man-pages --no-header-files --output <folder>`
- Use a JDK distribution that runs on old glibc (for example, Eclipse Temurin) as the jlink source. A JDK packaged by a Linux distribution requires that distribution's glibc
- Building with jlink's internal compression turned off and then packing everything with xz gives a smaller result
- Build a runtime shared by several parent skills from the union of all consumers' modules. If you trim native libraries further, verify with every consumer

At activation, extract the runtime into the working path and set the execute permission on the java executable. Announce the path through PATH or JAVA_HOME, or connect it through the settings variable of the library that calls Java.

In containers without a locale, Korean and other non-ASCII characters in Java output turn into question marks. Set LANG=C.UTF-8.

## Office application extensions

Download LibreOffice extensions (.oxt) from the official extension site or the project's releases.

- LibreOffice refuses per-user installation for the root user. As root, install with `unopkg add --shared <file>`, which needs write permission on the LibreOffice installation folder
- As a non-root user, pass the same dedicated profile path `-env:UserInstallation=file:///<path>` to both unopkg and soffice
- Extensions written in Java need a Java runtime for LibreOffice. If the system has no Java, point to the bundled runtime with `UNO_JAVA_JFW_JREHOME=file:///<runtime path>`
- File names with characters outside ASCII, such as Korean, open under a UTF-8 locale (LANG=C.UTF-8)

## Operating system packages

Use deb and rpm packages only when the target environment runs the same distribution and version. To use them without root, extract the package into the working path (`dpkg-deb -x <file> <folder>`) and set PATH and LD_LIBRARY_PATH. Check with `ldd <executable>` that the needed shared libraries exist in the target environment. If the distribution differs or is unknown, look first for another channel, such as a language package or a static build.

## Fonts

Bundle only fonts whose license allows redistribution (such as the SIL Open Font License). When a document names a commercial font, bundle a similar free font and connect it as a substitute.

- If the tool offers a font path option, use that option
- Without such an option, copy the fonts to `$HOME/.local/share/fonts` and run `fc-cache`. If HOME is not writable, write a fontconfig settings file that adds the font folder and a writable cache folder, and point FONTCONFIG_FILE at it
- When a document uses several families, such as serif and sans-serif, bundle a font for each family. If space runs short, assign one font as the substitute for several families. Without a substitute mapping, the output is missing the text in the unmapped family

## Model weights and data

Find in the code the repository names and cache paths of models and data the parent skill downloads on first run.

If they fit, download them into a local folder in the build environment and bundle them. At activation, connect the local path to the parent skill and set the offline mode environment variables. Hugging Face libraries use HF_HUB_OFFLINE=1.

Supply models in the GB range through a hybrid setup. The deep learning framework that runs the model can itself reach hundreds of MB, so count it as well.

Old model repositories sometimes fail to load in newer library versions. Record in the manifest the library version that passed verification together with the model.
