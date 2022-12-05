{
  "targets": [
    {
      "target_name": "SimpleDLL",
      "sources": [
        "SimpleDLL.cxx"
      ],
      "include_dirs": [
        "<!(node -e \"require('node-gyp-build')\")"
      ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "defines": [ "_UNICODE", "ADD_EXPORTS" ],
      "type": "shared_library"
    }
  ]
}
