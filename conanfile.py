from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.files import copy

required_conan_version = ">=1.50.0"

class mlConan(ConanFile):
    name = "ccache"
    url = "https://github.com/xlabmedical/ccache"
    description = "Compiler cache"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def export_sources(self):
        copy(self, "*", self.recipe_folder, self.export_sources_folder, excludes="conanfile.py")

    def layout(self):
        cmake_layout(self)

    def source(self):
        pass

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["ENABLE_TESTING"] = False
        tc.cache_variables["ENABLE_DOCUMENTATION"] = False
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_id(self):
        self.info.settings.rm_safe("compiler")
        self.info.settings.rm_safe("build_type")