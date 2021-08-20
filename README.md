# ff13_dds_replacer
Reimports DDS textures from imgb (image resources of final fantasy 13)
<br>

## Usage
`imgb_replace.exe imgb old_dds new_dds`
+ imgb: imgb file you want to edit
+ old_dds: DDS file you want to replace with new_dds
+ new_dds: DDS file you want to replace old_dds with
+ --overwrite: overwrite the imgb file (if false, generate a new imgb file)
+ --silent: show nothing except error messages

### example

```
set imgb=c201\bin\c201.win32.imgb
set old_dds=c201\bin\c001C_01.dds
set new_dds=mod.dds

imgb_replace.exe %imgb% %old_dds% %new_dds% --overwrite
```

### how it works

1. search imgb and find the same binary data as old_dds
2. replace the binary data with new_dds

### notation
+ 2 DDS files should be the same file size. (So, you can't change the resolution with this tool.)
+ When you edit DDS images, you should check export options carefully. It might change the file size.

## How to Get DDS
1. extract .imgb and .trb with [ff13tool](https://steamcommunity.com/app/292120/discussions/0/613939294277998633/)
2. rename `*.win32.imgb` and `*.win32.trb` to `*.ps3.imgb` and `*.ps3.trb`
3. export .dds from `*.ps3.trb` with [noesis](http://richwhitehouse.com/index.php?content=inc_projects.php&showproject)

## How to Bring .imgb to Game
you can reimport new .imgb with [ff13tool](https://steamcommunity.com/app/292120/discussions/0/613939294277998633/)<br>
I don't know why but you need to reimport .trb too.<br>
Here is an example.

```
set ff13filepath=D:\SteamLibrary\steamapps\common\FINAL FANTASY XIII\
set file=chr\pc\c201\bin\c201.win32
ff13tool -i -ff13 "%ff13filepath%white_data\sys\filelist_scrc.win32.bin" "%ff13filepath%white_data\sys\white_scrc.win32.bin" %file%.imgb
ff13tool -i -ff13 "%ff13filepath%white_data\sys\filelist_scrc.win32.bin" "%ff13filepath%white_data\sys\white_scrc.win32.bin" %file%.trb
```
