import os
import re

file_path = "/Users/ff/Desktop/maps/en_US_maps_dtail_2.txt"
# address = "/Users/ff/Desktop/测评数据/去空格/address.txt"
address_c = set()
address_c_lower = set()
address_y = set()
address_y_lower = set()
address_n = set()
address_n_lower = set()
address_z = set()
address_z_lower = set()
address_b = set()
address_b_lower = set()
address_s = set()
address_s_lower = set()
address_t = set()
address_t_lower = set()
address_p = set()
address_p_lower = set()
address_all_set = [{"country": address_c}, {"city": address_y}, {"noun": address_n}, {"build": address_b}
    , {"province": address_p}, {"zip": address_z}, {"street": address_s}, {"town": address_t}]
centence_original = {}

regex = re.compile('\s+')

data_folder = "/Users/ff/Desktop/maps/maps"
names = []


# string="hh hh ?? ?! ????AAA    ?  ?  A ??"
# ss=re.findall(regex,string)
# for s in ss:
#     string=string.replace(re.sub('\s+',string),'')
# print(string)
def getAllFile():
    # 无后缀
    for dir_path, subpaths, files in os.walk(data_folder):
        for name in files:  # 文件夹下的所有文件
            if not name.endswith('.DS_Store'):
                file_path = os.path.join(dir_path, name)
                names.append(name)
    for name in names:
        file_path = os.path.join(data_folder, name)
        # print(file_path)
        with open(file_path, 'r', encoding='utf-8') as f_add:
            for line in f_add:
                # ads = line.split('\t')
                if name == "country":
                    if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_c:
                        address_c.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                        address_c_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                if name == "city":
                    if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_y:
                        address_y.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                        address_y_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                if name == "noun":
                    if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_n:
                        address_n.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                        address_n_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                if name == "zip":
                    if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_z:
                        address_z.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                        address_z_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                if name == "build":
                    if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_b:
                        address_b.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                        address_b_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                if name == "street":
                    if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_s:
                        address_s.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                        address_s_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                if name == "town":
                    if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_t:
                        address_t.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                        address_t_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                if name == "province":
                    if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_p:
                        address_p.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                        address_p_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")


# print(address_t,address_s,address_z)

def makeMark():
    with open(file_path, 'r', encoding='utf-8') as f_in:
        for line in f_in:

            line = re.sub('\s+', ' ', line)
            line_original = line
            # print(line)
            for dict_s in address_all_set:
                # print(s.items())
                for dict_c in dict_s.items():
                    # print(dict_c[0])
                    for c in dict_c[1]:
                        # print(dict_c[0],c)
                        # print(line.lower().index(c.lower()))
                        if c.lower() in line.lower():
                            # if re.search(line.lower(),centence_original.keys(),re.IGNORECASE):
                            if line.lower() not in centence_original.keys():
                                # print("c", c)
                                start=int(line.lower().index(c.lower()))
                                # print(start,line[start:start+len(c.lower())].strip())
                                line = line.replace(line[start:start+len(c.lower())].strip(), re.sub('\s+', '#kika_' + dict_c[0] + '#', line[start:start+len(c.lower())].strip()))
                                centence_original[line_original.lower()] = line
                                # print(line)
                            else:
                                # print("c", c)
                                start = line.lower().index(c.lower())
                                # print(start,line[start:start+len(c.lower())].strip())
                                # print(start)
                                line = centence_original[line_original.lower()].replace(line[start:start+len(c.lower())].strip(),
                                                                                        re.sub('\s+', '#kika_' + dict_c[
                                                                                            0] + '#', line[start:start+len(c.lower())].strip()))
                                centence_original[line_original.lower()] = line
                                # print(line)


def centenceMark(i):
    for centence in centence_original.items():
        centence_o = centence[1]
        # print(centence_o)
        centence_o=re.sub("#kika_\w+#",' ',centence_o)
        centence_o = re.sub("\s+", ' ', centence_o)
        # print(centence_o)
        centence = centence[1]
        # print("line", centence)
        centence = re.sub('\s+', ' ', centence)
        line = regex.split(centence.strip())
        ll = []
        # print(len(line))
        for l in line:
            # print(l)
            if " " + l.lower() + " " in address_c_lower:
                ll.append(l + "\t" + "B-country")
            elif " " + l.lower() + " " in address_y_lower:
                ll.append(l + "\t" + "B-city")
            elif " " + l.lower() + " " in address_n_lower:
                ll.append(l + "\t" + "B-noun")
            elif " " + l.lower() + " " in address_b_lower:
                ll.append(l + "\t" + "B-build")
            elif " " + l.lower() + " " in address_z_lower:
                ll.append(l + "\t" + "B-zip")
            elif " " + l.lower() + " " in address_p_lower:
                ll.append(l + "\t" + "B-province")
            elif " " + l.lower() + " " in address_s_lower:
                ll.append(l + "\t" + "B-street")
            elif " " + l.lower() + " " in address_t_lower:
                ll.append(l + "\t" + "B-town")
            elif "#kika_" in l:
                # print("1111111")
                ll_country = list(filter(None, l.strip().split("#kika_country#")))
                # print(len(ll_country))
                ll_city = list(filter(None, l.strip().split("#kika_city#")))
                # print(len(ll_city))
                ll_noun = list(filter(None, l.strip().split("#kika_noun#")))
                ll_build = list(filter(None, l.strip().split("#kika_build#")))
                ll_zip = list(filter(None, l.strip().split("#kika_zip#")))
                ll_province = list(filter(None, l.strip().split("#kika_province#")))
                ll_street = list(filter(None, l.strip().split("#kika_street#")))
                ll_town = list(filter(None, l.strip().split("#kika_town#")))
                # print(ll_noun)
                # print(len(ll_noun))
                ll_all_array = [{"country": ll_country}, {"city": ll_city}, {"noun": ll_noun}, {"build": ll_build}
                    , {"province": ll_province}, {"street": ll_street}, {"town": ll_town}, {"zip": ll_zip}]
                for ll_all_dict in ll_all_array:
                    for ll_dict in ll_all_dict.items():
                        # for ll_all in ll_dict[1]:
                        if len(ll_dict[1]) != 1:
                            for i_all in range(0, len(ll_dict[1])):
                                # print(i_country)
                                if i_all == 0:
                                    ll.append(ll_dict[1][i_all] + "\t" + "B-" + ll_dict[0])
                                elif i_all == len(ll_dict[1]) - 1:
                                    ll.append(ll_dict[1][i_all] + "\t" + "E-" + ll_dict[0])
                                else:
                                    ll.append(ll_dict[1][i_all] + "\t" + "I-" + ll_dict[0])

            else:
                ll.append(l + "\t" + "U")
        with open(file_path.replace(".txt", ".mark"), 'a', encoding='utf-8') as f_out:
            if "country" in "\t".join(ll) or "city" in "\t".join(ll) or "build" in "\t".join(ll) or "town" in "\t".join(
                    ll) \
                    or "province" in "\t".join(ll) or "zip" in "\t".join(ll) or "street" in "\t".join(ll):
                i += 1
                # f_out.write(str(i)+":\t\t"+centence_o.strip())
                f_out.write('\n')
                # ll=ll.split('\t')
                f_out_array={}
                for aa in range(0, len(ll)):
                    # print(ll[aa])
                    ll_aa=ll[aa].split('\t')
                    if aa < len(ll) - 1 and "noun" in ll[aa + 1] and ("E-" in ll[aa]):
                        ll[aa] = ll[aa].replace('E-','I-')
                        print("privious",ll[aa])
                        f_out_array[ll_aa[0]]=ll[aa]
                        f_out.write(ll[aa].strip())
                        f_out.write('\n')
                    if "noun" in ll[aa] and aa > 0 and (
                            "country" in ll[aa - 1] or "city" in ll[aa - 1] or "build" in ll[aa - 1]
                            or "town" in ll[aa - 1] or "province" in ll[aa - 1] or "zip" in ll[aa - 1]
                            or "street" in ll[aa - 1]):
                        privious = ll[aa - 1].split('\t')
                        ll[aa] = ll[aa].replace(ll[aa].split('\t')[1], privious[1].replace('B-', "E-"))
                        print("last",ll[aa])
                        # f_out_array.append(ll[aa].strip())
                        f_out_array[ll_aa[0]] = ll[aa]
                        f_out.write(ll[aa].strip())
                        f_out.write('\n')

                    # if "noun" in ll[aa] and aa > 0 and (
                    #         "country" in ll[aa - 1] or "city" in ll[aa - 1] or "build" in ll[aa - 1]
                    #         or "town" in ll[aa - 1] or "province" in ll[aa - 1] or "zip" in ll[aa - 1]
                    #         or "street" in ll[aa - 1]):
                    #     privious = ll[aa - 1].split('\t')
                    #     ll[aa] = ll[aa].replace(ll[aa].split('\t')[1], privious[1].replace('I-', "E-"))
                    #     print("last",ll[aa])
                    #     # f_out_array.append(ll[aa].strip())
                    #     f_out_array[ll_aa[0]] = ll[aa]
                    else:
                        print("original",ll[aa])
                        # f_out_array.append(ll[aa].strip())
                        f_out_array[ll_aa[0]] = ll[aa]
                        f_out.write(ll[aa].strip())
                        f_out.write('\n')
                # for f_out_ in f_out_array.items():
                #     print(f_out_[0],f_out_[1])
    print(i)


if __name__ == '__main__':
    i = 0
    getAllFile()
    makeMark()
    centenceMark(i)

    print("Finish line")
