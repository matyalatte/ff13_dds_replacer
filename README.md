# ff13_dds_replacer
Reimports DDS textures to imgb (image resources of Final Fantasy 13)<br>
<br>
<img src=replace_c002C_01.png width=480>
## Usage
`imgb_replace.exe imgb old_dds new_dds`
+ imgb: imgb file you want to edit
+ old_dds: DDS file you want to replace with new_dds
+ new_dds: DDS file you want to replace old_dds with
+ --overwrite: overwrite the imgb file (if false, generate a new imgb file)
+ --silent: show nothing except error messages

### example

```
set imgb=c202\bin\c202.win32.imgb
set old_dds=c202\bin\c002C_01.dds
set new_dds=mod.dds

imgb_replace.exe %imgb% %old_dds% %new_dds% --overwrite
```

### how it works

1. Open imgb and find the same binary data as old_dds
2. Replace the binary data with new_dds

### notation
+ 2 DDS files should be the same file size. (So, you can't change the resolution with this tool.)
+ When you edit DDS images with an image editor like GIMP, you should check export options carefully. It might change the file size.
+ This tool will work fine with FF13-2 and LRFF13. (I haven't test, though)

## Some Tips About FF13 Modding

### How to Get Original DDS
1. Extract .imgb and .trb with [ff13tool](https://steamcommunity.com/app/292120/discussions/0/613939294277998633/) 

```
set ff13filepath=D:\SteamLibrary\steamapps\common\FINAL FANTASY XIII\
ff13tool -x -ff13 "%ff13filepath%white_data\sys\filelist_scrc.win32.bin" "%ff13filepath%white_data\sys\white_scrc.win32.bin"
```

2. Rename `*.win32.imgb` and `*.win32.trb` to `*.ps3.imgb` and `*.ps3.trb`
3. Export .dds from `*.ps3.trb` with [noesis](http://richwhitehouse.com/index.php?content=inc_projects.php&showproject)

### How to Bring .imgb to Game
You can reimport new .imgb with [ff13tool](https://steamcommunity.com/app/292120/discussions/0/613939294277998633/)<br>
I don't know why but you need to reimport .trb too.<br>
Here is an example.

```
set ff13filepath=D:\SteamLibrary\steamapps\common\FINAL FANTASY XIII\
set file=chr\pc\c202\bin\c202.win32
ff13tool -i -ff13 "%ff13filepath%white_data\sys\filelist_scrc.win32.bin" "%ff13filepath%white_data\sys\white_scrc.win32.bin" %file%.imgb
ff13tool -i -ff13 "%ff13filepath%white_data\sys\filelist_scrc.win32.bin" "%ff13filepath%white_data\sys\white_scrc.win32.bin" %file%.trb
```

### How to Extract Audio Files
1. Extract .scd with [ff13tool](https://steamcommunity.com/app/292120/discussions/0/613939294277998633/).

```
set ff13filepath=D:\SteamLibrary\steamapps\common\FINAL FANTASY XIII\
ff13tool -x -ff13 "%ff13filepath%white_data\sys\filelistc.win32.bin" "%ff13filepath%white_data\sys\white_imgc.win32.bin"
```

2. Convert .scd to .wav with [foobar2000](https://www.foobar2000.org/download) and [vgmstream plugin](https://www.foobar2000.org/components/view/foo_input_vgmstream).

You can also use [vgmstream](http://hcs64.com/files/vgmstream/) and [vgmstream external ddl](http://hcs64.com/files/vgmstream_external_dlls.zip) to convert .scd , but this tool can't open some .scd files.
