import platform
from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager("morheit")
    builder.add({"arch": "x86_64", "build_type": "Release"})
    if (platform.system() == "Linux"):
        builder.add({"arch": "x86_64", "build_type": "Release"}, {"folly:shared": True})
    builder.run()
