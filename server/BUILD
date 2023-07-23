load("@rules_python//python:defs.bzl", "py_binary")
load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "app_server",
    srcs = ["app.py"],
    main = "app.py",
    visibility = ["//visibility:public"],
    deps = [
        requirement("Flask") 
    ],
)