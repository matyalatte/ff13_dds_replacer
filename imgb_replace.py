#FF13 DDS replacer for imgb by MatyaModding (2021/08/21)

import argparse,os

#-------------args and i/o
def get_args():
    parser = argparse.ArgumentParser() 
    parser.add_argument('imgb', help='imgb file you want to edit')
    parser.add_argument('old_dds', help='dds file you want to replace with new_dds')
    parser.add_argument('new_dds', help='dds file you want to replace old_dds with')
    parser.add_argument('--overwrite', action='store_true', help='overwrite imgb file')
    parser.add_argument('--silent', action='store_true', help='show nothing except error messages')
    args = parser.parse_args()
    return args

def print_args(args):
    print("imgb: "+args.imgb)
    print("old_dds: "+args.old_dds)
    print("new_dds: "+args.new_dds)
    print("overwrite: "+str(args.overwrite))
    print("silent: "+str(args.silent))

def print_(string, silent):
    if not silent:
        print(string)

#-------------read and write
def read_binary(file):
    f=open(file, 'rb')
    data = f.read()
    f.close()
    return data

#gets imgb file as binary data
def read_imgb_bin(file):
    if file[-5:]!=".imgb":
        raise Exception(file+" should be a imgb file.")
    return read_binary(file)

#gets dds image as binary data
#and separates it into header and raw data
def read_dds_bin(file):
    dds_bin=read_binary(file)

    #checks the format
    isDDS=dds_bin[:3]==b'DDS'
    if not isDDS:
        raise Exception(file+" should be a dds file.")
    isDXT1=dds_bin[84:88]==b'DXT1'
    if not isDXT1:
        raise Exception(file+" should be a DXT1 image.")
        
    head=dds_bin[:148]
    img=dds_bin[148:]
    return head, img

def write_binary(file, bin):
    f=open(file, "wb")
    f.write(bin)
    f.close

def write_new_imgb(file_name, new_imgb, overwrite):
    write_binary(file_name[:-5]+"new"*(1-overwrite)+".imgb", new_imgb)

#--------------main features
#replaces dds data in imgb
def replace_dds_in_imgb(imgb, old_img, new_img):
    count = imgb.count(old_img)
    if count==0:
        raise Exception("The data of old dds image does NOT exist in the imgb file.")
    if count>=2:
        raise Exception("There are two or more matched data in imgb. This is unexpected.")
    new_imgb = imgb.replace(old_img, new_img)
    return new_imgb

if __name__=="__main__":
    args=get_args()
    imgb_name=args.imgb
    old_dds_name=args.old_dds
    new_dds_name=args.new_dds
    overwrite=args.overwrite
    silent=args.silent
    if not silent:
        print("---DDS replacer for imgb by MatyaModding---")
        print_args(args)

    try:
        print_("loading files...", silent)
        imgb = read_imgb_bin(imgb_name)
        _, old_img = read_dds_bin(old_dds_name)
        _, new_img = read_dds_bin(new_dds_name)
        #checks the file size
        if len(old_img)!=len(new_img):
            raise Exception("2 DDS files should be the same size. old_dds is {} bytes, but new_dds is {} bytes.".format(len(old_img)+148,len(new_img)+148))

        print_("replacing the dds file in the imgb file...", silent)
        new_imgb = replace_dds_in_imgb(imgb, old_img, new_img)

        print_("saving new imgb file...", silent)
        write_new_imgb(imgb_name, new_imgb, overwrite)

        print_("done!", silent)

    except FileNotFoundError as e:
        if silent:
            print_args(args)
        print(e.args[1])
        print("DDS replacement is canceled.")

    except Exception as e:
        if silent:
            print_args(args)
        print("ERROR: "+e.args[0])
        print("DDS replacement is canceled.")

    print_("-------------------------------------------", silent)

    


