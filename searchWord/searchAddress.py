inputpath = "/Users/ff/Desktop/测评数据/特殊词汇占比"
unigrampath = "/Users/ff/Desktop/测评数据/maps/address_unigram"
outpath = "/Users/ff/Desktop/测评数据/maps/out.txt"
unigramset = ["Nazi", "Nazis", "Nazizeit", "Nazideutschland", "Hitler", "Hitlers"
    , "Hitlergruß", "Führer", "Auschwitz", "Neonazi", "Minderrassige", "Sonderbehandlung", "Mischehe", "Vergasung",
              "vergasen", "Holocaust", "arisch", "Rassenschande", "Eintopf", "Betreuungseinrichtungen",
              "Konzentrationslager", "Hakenkreuz", "NSDAP", "Goebels", "Judenfrei", "Judenfeindlich", "Neonazis"]

def ifcontains(input, out):
    with open(input, 'r', encoding='utf-8') as f_input:
        with open(out, 'w', encoding='utf-8') as f_out:
            for line in f_input:
                for unigram in unigramset:
                    if (" " + unigram + " ") in (" " + line.strip().lower() + " "):
                        # print(unigram + "\t" + line.strip())
                        f_out.write((unigram + "\t" + line.strip()).strip())
                        f_out.write("\n")
                        break


# def getoutcontent(out):
if __name__ == '__main__':
    ifcontains(inputpath, outpath)
    print("Finish line")
