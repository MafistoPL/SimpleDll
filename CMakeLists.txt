cmake_minimum_required(VERSION 3.10)

project(SimpleDLLProj)

add_compile_definitions(ADD_EXPORTS)

add_library(SimpleDLL SHARED
  "SimpleDLL.cxx"
  "SimpleDLL.h")
