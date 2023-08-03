py_library(
    name = "rand_gen_lib",
    srcs = ["rand_gen.py"],
    visibility = ["//:__subpackages__"],
)

py_test(
    name = "rand_gen_test",
    srcs = ["rand_gen_test.py"],
    deps = [":rand_gen_lib"],
)
