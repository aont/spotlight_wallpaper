@echo off
set SHOBJIDL_IDL=c:/msys64/mingw64/x86_64-w64-mingw32/include/shobjidl.idl
midl.exe "%SHOBJIDL_IDL%" /tlb shobjidl.idl