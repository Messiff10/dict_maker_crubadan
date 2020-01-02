import re

pattern_url = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

pattern_delete = re.compile("%")   # 需要去掉的特殊符号

pattern_continuousNum = re.compile(r'\d{4,}')

pattern_brackets = re.compile(r'（.*）')
pattern_bracket_left = re.compile(r'（.*）?')
pattern_bracket_right = re.compile(r'（?.*）')

# 可以匹配这些形式的phone number：5-161-112222 516-1112222 (516)111-2222 5161112222 516-111-2222 13445545654
pattern_phoneNum = re.compile(r"(\+420)?(\s*)?((\()?(\d{1})?-?(\d{3})(\s*)?-?(\))?(\d{3,6})(\s*)?-?(\d{4})?)")


pattern_password = re.compile(r'''
                        (?=^.{6,}$)     # 六位数及以上
                        (?=.*\d+)     # 至少一位数字
                        (?![.\n])       # 没有换行符
                        (?=.*[A-Za-z]).*$  # 大小写任意个
                    ''', re.VERBOSE)
# 邮箱
pattern_email = re.compile(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}')

pattern_at = re.compile(r'@[ ]*[0-9a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒąćęłńóśźżĄĆĘŁŃÓŚŹŻàèéìíîòóùúÀÈÉÌÍÎÒÓÙÚáéíñóúüÁÉÍÑÓÚÜа-яА-Я\u0627-\u064a]+')

# noCharacters：键盘上没有的符号
# 英语
en_US_noCharacters = re.compile(r"[^q1w2e3èéēêër4t5y67uûúūüùiî8íìïīo9óôöòœøōõp0)l(k+j\-h&g%f$d#ßs@aàáâäæãåāz*x\"c'v:ç"
                                r";b!nñm¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅\]}>{<\[±_—–·‰¢€₱£¥†‡★“”„«»’‘‚‹›¡¿?/.~`|♪•♣♠♥♦√πΠ÷×§¶∆"
                                r"≠=≈∞′°″↑^←↓→\\©®™℅≤≥,…\s]+")
# 英式英语
en_GB_noCharacters = re.compile(r'[^q1w2e3èéēêër4t5y6u7ûúùūi8îíīïìo9óôöòœøōõ0p)l(k+jh&g%f$d#sßa@àáâäæãåā*z"x\'cç:v;'
                                r'b!nñ?m¹½⅓¼⅛²⅔³¾⅜⁴⅝⅞ⁿ∅\]}>{<\[±_\-—–·‰¢£¥€₱†‡★“„”«»’‘‚‹›¡¿/,….~`|♪•♠♣♥♦√πΠ÷×§¶∆≠=≈'
                                r'∞′°″↑^←↓→\\®©™℅≤≥\s]+')
# 法国
French_noCharacters = re.compile(r"[^aàâ1æáäãåāªz2e3êéèëēęėr4t5y6ÿu7ùûúüūi8îïìįíīo9ôœöòóõøōºp0qsdfghjklmwxcçčćvbn'›‹’‘"
                                 r"‚¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#€₱$¢£¥‰%&\-—_–·+±{<\[()\]}>*†‡★\"„“”«»:;¡!¿?~`\|•♣♠"
                                 r"♪♥♦√Ππ÷×§¶∆^←↑↓→′″°∞=≠≈\\©®™℅≤≥…,\s]+")
# 德国
German_noCharacters = re.compile(r"[^q1w2e3èéėêër4t5zu7ûüūùúioöôòóõœøōp0lkjhgfdßäsšśaâàáāåæyxcvbñnńm¹½⅓¼⅛²⅔³⅜¾⁴⅝6⅞89ⁿ"
                                 r"∅\])}>{<\[(±+_—–·&‰%¢€£¥$₱#@†‡★*„”“\"»«‘‚’›‹:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§∆¶≠=≈∞′″°↑←^↓"
                                 r"→\\©®™℅≤≥\s]+")
# 波兰
Polish_noCharacters = re.compile(r"[^q12w3eèęéėêëēr45ty7iùūûúüoóöôòõœøōp0łlkjhgfdśsßšąaáàâäæãåāżzźžxćcčçbvńnñm¹½⅓¼⅛²⅔"
                                 r"³⅜¾⁴⅝6⅞89ⁿ∅\])}>{<(\[±+_\-—–·&‰%¢$£¥€₱#@†*‡★„“\"”«»'’‚‘‹›:;¡!¿?/,….~`|♪♣♠♥♦•√÷πΠ×§"
                                 r"¶∆≠=≈∞′″↑^←↓→°\\©®™℅≤≥\s]+")
# 意大利
Italian_noCharacters = re.compile(r"[^q1w2e3éèêėëęēr4t5y6u7úùūûüi8ìíîįïīo9òóôöõœøōºp0aàáâäæãåāªsdfghjklzxcvbnm¹½⅓¼⅛²⅔³"
                                  r"¾⅜⁴⅝⅞ⁿ∅@#€₱$¢£¥%‰&_\-—–·+±(<{\[)\]}>*†‡★\"„“”«»'‚‘’‹›:;!¡?¿/,.…~`|•♣♠♪♥♦√πΠ÷×§¶∆≠="
                                  r"≈∞°′″↑↓→←^\\©®™℅≥≤\s]+")
# 西班牙
Spanish_noCharacters = re.compile(r"[^q1w2e3èéëėêęēr4t5y6u7üúûùūi8íïìįîīo9óòöôõøœōºp0aáàäâãåąæāªsdfghjklñzxcçčćvbnńm?."
                                  r",!;¿@¡:¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅)\]}>(<{\[+±\-_—–·&%‰€¥£¢$₱#*†‡★\"“„”«»'’‹›‘‚~`|♪•♣♠♥♦√Ππ÷×§"
                                  r"¶∆≠=≈∞°′″^↑←↓→\\©®™℅\s]+")
# 俄语
Russian_noCharacters = re.compile(r"[^й1ц2у3́к4е5́ён6г7ш8щ9з0хэ́эждло́орпа́авы́ыфячсмитъьбю¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅\])>}{\[<(±+_\-—–"
                                  r"·&‰%¢$£¥₱€#@†*‡★„\"”“«»‘‚’‹›':;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←↓→\\©®™℅\s]+")

# 阿拉伯语
Arabic_noCharacters = re.compile(r'[^ض1١ص2٢ث3٣ق4ڨ٤ف5٥ڢڤڥغ6٦ع7٧ه8‍٨خ9٩ح0٠جچشڜسيئىبپلاإأآءٱتنمگكکطذؤرةوژزظد'
                                 r',ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢$₱€£¥%٪‰&_\-—–·+±)}>﴿({<﴾*★٭"„“”»«\'‚‘’›‹:;؛¡!?؟ '
                                 r'/،.~`|♪•√πΠ÷×§¶∆≠≈∞′″←↑↓→^\\©®™℅\]\[\s]+')

# nl--Dutch 荷兰语
Dutch_noCharacters = re.compile(r'[^qweëéêėèęērtyĳuüúūûiùíïīîįoóöôòõœøōpaáäâàæãåāsdfghjklzxcvbñńm1¹½⅓¼⅛2²⅔3³¾⅜4⁴5⅝67⅞8'
                                r'9ⁿ0@#¢€₱$£¥‰%&_—–·\-±+{(<\[)\]}>*†‡★„"“”«»\'’‘‚‹›:;¡!¿?/,.…~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑'
                                r'^←↓→\\©®™℅≤≥\s]+')

# cs_CZK 捷克语 Czech
Czech_noCharacters = re.compile(r'[^q1w2e3ěéèêēėęër4ř5tťz6źžżu7ůúûüùūi8íîïīìįo9óöôòõœøōp0lkjhgfďdšsßśaáàâäæãåāýyÿxčcćç'
                                r'vbňnńñm¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅\])}>{<\[(+±_\-—–·&‰%¢$£¥€₱#@†*‡★„"”“»«‘‚\'’›‹:;¡!¿?,/….~`|♪•♣'
                                r'♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←↓→\\©®™℅≤≥\s]+')

# tr--土尔其
Turkish_noCharacters = re.compile(r'[^qw3e4r5ty7uûüūùúi8îïıíìįīo9öôœòóõøō0plkjhğgfdşsśßšâazxçcčćvbnm1¹½⅓¼⅛2²⅔³⅜¾⁴⅝6⅞ⁿ∅'
                                  r'\])}>{<\[(+±_—–·\-&‰%¢₺£€₱¥$#@†‡★*“"„”«»’\'‘‚‹›:;¡!¿?~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞°′″↑^←↓→'
                                  r'\\©®™℅≤≥,….\s]+')

# urdu--乌尔都语
Urdu_noCharacters = re.compile(r'[^ق١1و٢2٣ع3ر٤4ت٥5ے٦6ء٧7ى٨8ه٩9پ٠0لکجحگفدسازشچطبنم¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅\])}>({\[<+±\-_—–·：'
                               r'‰%¢$£¥€₱#@†*‡★"„“”«»’‚‘\'‹›؛¡！¿؟/،.…~`|♪•♣♠♥♦√πΠ÷§×¶∆≠=≈∞′°″↑^←↓→\\©®™℅≤≥'
                               r'ْؤٰڑٹَأئةۀُخضھغًڈصآذژثظِںّ\s]+')
Urdu_Characters = re.compile(r'[ق١1و٢2٣ع3ر٤4ت٥5ے٦6ء٧7ى٨8ه٩9پ٠0لکجحگفدسازشچطبنم¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅\])}>({\[<+±\-_—–·：'
                               r'‰%¢$£¥€₱#@†*‡★"„“”«»’‚‘\'‹›؛¡！¿؟/،.…~`|♪•♣♠♥♦√πΠ÷§×¶∆≠=≈∞′°″↑^←↓→\\©®™℅≤≥'
                               r'ْؤٰڑٹَأئةۀُخضھغًڈصآذژثظِںّ\s]+')

# ro -- 罗马尼亚语
Romanian_noCharacters = re.compile(r'[^qwertțyu7iîïìīíįoplkjhgfdșsßšśaâãăàáäåāzxcvbnm¹1½⅓¼⅛2²⅔3³⅜¾4⁴⅝56⅞89ⁿ∅0\])'
                                   r'}>([{<±+_\-—–·&‰%¢$£¥€₱#@†*‡★„“”«»’\'‚‘‹›:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′″↑'
                                   r'^←↓→¥€¢£\\©®™℅≤≥\s]+')

# fa -- 波斯语
Farsi_noCharacters = re.compile(r'[^ض۱ص۲ث۳ق۴فغ۶6ع۷7ه8ةه‍ٔ۸خ۹9ح۰0جگكک‌منتآ'
                                r'اإأءٱلبئيىیسشظطژزرذدپؤوچ،,.1¹½⅓¼⅛2²⅔¾3³⅜4⁴۵5⅝⅞۰٫٬ⁿ∅[({<﴾)}\]>﴿±+_\-'
                                r'—–·&%٪‰﷼¢$€¥£#@★*٭„«“”»‚‘’›‹:;؛¡!?؟/ًٌٍّْٕٔـََُُٰٖ~`|♪•√πΠ÷×§¶∆≠≈∞′″°↑←^↓→\\©®™℅≥≤\s]+')

# uk -- 乌克兰语
Ukrainian_noCharacters = re.compile(r'[^Й1ц2у3к4е5н6г7ґш8щ9з0хфіївапролджєюбъьтимсчя¹½⅓¼⅛²⅔³¾⅜⁴⅝⅞ⁿ∅\])}>('
                                    r'[{<±+_\-—–·&‰%$₴¢€¥£₱#@†*‡★„"”“«»‘‚’\'‹›:;¡¿!?_/,….~`|♪•♠♣♥♦√πΠ÷×§¶∆'
                                    r'≠=≈∞↑^←↓→\\©®™℅≤≥\s]+')

# pt_PT -- 欧洲葡萄牙语
EuropeanPortuguese_noCharacters = re.compile(r'[^1qw2e3êéèëėęēr4t5y6u7üúûùūi8íîìįīo9óõôòöœøōºp0lkjhgfdsaáãâªæå'
                                             r'äzxçcćčvbnm¹½⅓¼⅛²⅔³⅜¾⁴⅝6⅞89ⁿ∅\]}>[{<±+_—\-–·&‰%¢€£¥$₱#@†*‡★„“"'
                                             r'”«»’\'‘‚‹›:;¡!¿?/,….~`|♪•♠♣♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←↓→\\©®™℅≥\s]+')

# ms_MY -- 马来西亚语
Malay_noCharacters = re.compile(r'[^q1w2e3r4t5y6u7i8o9p0asdfghjklzxcvbnm, .:\'@#!?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ$₱€¢£¥%‰&\-—'
                                r'_–·+±(<{[)>}\]*†‡★"„“”«»\'‚‘’‹›;¡¿/…~`|•♣♠♪♥♦√Ππ÷×¶§∆^←↑↓→°′″=∞≠≈\\©®™℅≤≥\s]+')

# tl -- 菲律宾语：他加禄语
Tagalog_noCharacters = re.compile(r'[^q1w2eə3èér4t5y6uü7ùúiı8íoöò9p0aáàsşdfgğhjklzxcçvbnñm, .-:\'@#!?¹½⅓¼⅛²'
                                  r'⅔⅜³¾⁴⅝⅞∅ⁿ$₱€¢£¥%‰&\-—_–·+±(<{[)>}\]*†‡★"„“”«»\'‚‘’‹›:;¡¿/.…~`|•♣♠♪♥♦√Ππ'
                                  r'÷×¶§∆^←↑↓→°′″=∞≠≈\\©®™℅≤≥\s]+')

# hu -- 匈牙利语
Hungarian_noCharacters = re.compile(r'[^q1w2eėëęēè3éêr4t5z6uûùūü7úűiīìįïî8íoōøœõòôőöó9p0aæãåāáàâäsdfghjklyx'
                                    r'cvbnm, .\-:\'@#!?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ$₱€¢£¥%‰&—_–·+±(<{[)>}\]*†‡★"“„”»«‘‚’'
                                    r'›‹;¡¿/…~`|•♣♠♪♥♦√Ππ÷×¶§∆^←↑↓→°′″=∞≠≈\\©®™℅≤≥\s]+')

# th -- 泰语
Thai_noCharacters = re.compile(r'[^ๅ1/2๑_3๒ภ4๓ถ5๔ ุ ึ ค6๕ต7๖จ8๗ข๘9ช0๙ๆ๐ไ ำพะ ั ี รนยบลฟหกดเ ้ ่ าสวงฃผปแอ ิ ื ทมใฝ, .'
                               r'\-:\'@#!?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ฿₱£¥€$¢%‰&—–·+±(<{[)>}\]*†‡★"„“”«»‚‘’‹›;¡¿…~`|•♣♠'
                               r'♪♥♦√Ππ÷×§¶∆←↑↓→^′″°∞≠≈=\\©®™℅≤≥\s]+')

# fi -- 芬兰语
Finnish_noCharacters = re.compile(r'[^q1w2e3r4t5y6u7üi8oōœóõòô9øp0åaâãāæàásšßśdfghjklöäzżžźxcvbnm, .\-:\'@'
                                  r'#!?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ€₱$¢£¥%‰&—_–·+±(<{[)>}\]*†‡★"„“”«»‚‘’‹›;¡¿/…~`|•♣♠♪♥'
                                  r'♦√Ππ÷×¶§∆^←↑↓→°′″=∞≠≈\\©®™℅≤≥\s]+')

# vi -- 越南语
Vietnamese_noCharacters = re.compile(r'[^q1w2eễếểệêẽẹềé3èẻr4t5yỵỷỹý6ỳuữứửựưũụừú7ùủiịỉĩí8ìoợỡởớờơộỗổốồôọõỏó'
                                     r'ò9p0aẫậặâầấẩăằắẳẵàáảãạsdđfghjklzxcvbnm, .\-:\'@#!?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ₫₱'
                                     r'£¥€$¢%‰&—_–·+±(<{[)>}\]*†‡★"„“”«»‚‘’‹›;¡¿/…~`|•♣♠♪♥♦√Ππ÷×¶§∆^←↑↓→°′'
                                     r'″=∞≠≈\\©®™℅≤≥\s]+')

# sv -- 瑞典语
Swedish_noCharacters = re.compile(r'[^q1w2eęêëè3ér4řtþ5ťyÿ6ýuūùûú7üiïì8íîoōôõò9óp0åaáàâąãsśšşßdðďfghjklłöœø'
                                  r'äæzżźžxcčçćvbnňńñm, .\-:\'@#!?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ€₱$¢£¥%‰&—_–·+±(<{[)>}\]*†'
                                  r'‡★"„“”»«‚‘’›‹;¡¿/…~`|•♣♠♪♥♦√Ππ÷×¶§∆^←↑↓→°′″=∞≠≈\\©®™℅≤≥\s]+')

# kk -- 哈萨克语
Kazakh_noCharacters = re.compile(r'[^й1ц2уұ3үк4қе5ён6ңг7ғш8щ9з0хфыіваәпроөлджэһячсмитьъбю, .\-:\@#!?¹½⅓¼⅛²⅔'
                                 r'⅜³¾⁴⅝⅞∅ⁿ$₱€¢£¥%‰&—_–·+±(<{[)>}\]*†‡★"„“”«»‚‘’‹›;¡¿/…~`|•♣♠♪♥♦√Ππ÷×¶§∆^←↑'
                                 r'↓→°′″=∞≠≈\\©®™℅≤≥\s]+')

# da -- 丹麦语
Danish_noCharacters = re.compile(r'[^q1w2eë3ér4t5yÿ6ýuūûùü7úiï8íoōõœòô9óp0åaâãāáäàsßśšdðfghjklłæøözxcvbnñńm'
                                 r', .\-:\'@#!?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ€₱$¢£¥%‰&—_–·+±(<{[)>}\]*†‡★"”„“»«’‚‘›‹;¡¿/…~'
                                 r'`|•♣♠♪♥♦√Ππ÷×¶§∆^←↑↓→°′″=∞≠≈\\©®™℅≤≥\s]+')

# nb -- 挪威语
Norwegian_noCharacters = re.compile(r'[^q1w2eėëęēè3éêr4t5y6uūùúû7üi8oōœöõóò9ôp0åaâãāàäásdfghjkløæzxcvbnm, .'
                                    r':\'@#!?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ$₱€¢£¥%‰&\-—_–·+±(<{[)>}\]*†‡★"“„”«»‘‚’‹›;¡¿/…~'
                                    r'`|•♣♠♪♥♦√Ππ÷×¶§∆^←↑↓→°′″=∞≠≈\\©®™℅≤≥\s]+')

# Burmese 缅甸语 my_MM
Burmese_noCharacters = re.compile(r'[^၁၂၃၄၅၆၇၈၉၀စသငကပအမနတဆေ်ိ္ါ့ျုူးၮဈၦၧၱၲႏၯၷၼႊၸ႕ၠႈႆဦဏၥၰၵဒဓဴဳႉၾၿႀဲြ႕႔ံႍႋႌႎၤၳဌီၽွႇဗဧဇၹၨၳဌၴ႒ၭဃၣၡဠႅဝၻဉ၏။\s]+')
Burmese_Characters = re.compile(r'[၁၂၃၄၅၆၇၈၉၀စသငကပအမနတဆေ်ိ္ါ့ျုူးၮဈၦၧၱၲႏၯၷၼႊၸ႕ၠႈႆဦဏၥၰၵဒဓဴဳႉၾၿႀဲြ႕႔ံႍႋႌႎၤၳဌီၽွႇဗဧဇၹၨၳဌၴ႒ၭဃၣၡဠႅဝၻဉ၏။\s]+')


# 印地语 hi
India_noCharacters = re.compile(r'[^१1⅓¼⅛¹½2²⅔२३¾3³⅜४4⁴५5⅝६67⅞७8८9९0∅ⁿ@#€¢£¥₱$%‰&—_–·\-+±(<{[\]}>)/★†‡*„“”«»"\'‚‘’‹›:;¡!¿?_, ….'
                                r'~`|♪♣♠♥♦•√πΠ÷×§¶∆£€¥¢←↑↓→^′″°∞≠≈={},\©®™℅[\]‹≤«<>›≥» ….'
                                r'\u0948\u0947\u0942\u0941\u094b\u094c\u093f\u0940\u0902\u093c\u0948\u0947'
                                r'\u0942\u0941\u094b\u094c\u093f\u0940\u0902\u093c\u0948\u0967\u0973\u0976'
                                r'\u0977\u0967\u0947\u0968\u0974\u0911\u0972\u0968\u0942\u0969\u0969\u0941'
                                r'\u096a\u0941\u096a\u094b\u096b\u096b\u094c\u096c\u096c\u093f\u096d\u090d'
                                r'\u096d\u0940\u096e\u090e\u096e\u0902\u096f\u0904\u0912\u096f\u093c\u0966'
                                r'\u0975\u0966\u0905\u0967\u0948\u0973\u0976\u0977\u0967\u0906\u0968\u0947'
                                r'\u0974\u0911\u0972\u0968\u0907\u0969\u0942\u0969\u0908\u096a\u0941\u096a'
                                r'\u0909\u096b\u094c\u096b\u090a\u096c\u094b\u096c\u090f\u096d\u093f\u090d'
                                r'\u096d\u0910\u096e\u0940\u090e\u096e\u0913\u096f\u0902\u0904\u0912\u096f'
                                r'\u0914\u0966\u093c\u0975\u0966\u090b\u0919\u093e\u0a3e\u094e\u0962\u0963'
                                r'\u0915\u094d\u0937\u0949\u0943\u0933\u0934\u0955\u0945\u094d\u093b\u090b'
                                r'\u0919\u093e\u0a3e\u094e\u0962\u0963\u0915\u094d\u0937\u0949\u0943\u0933'
                                r'\u0934\u0955\u0945\u094d\u093b\u0915\u0915\u094d\u0930\u0915\u094d\u092f'
                                r'\u0915\u094d\u0938\u0915\u094d\u0932\u0958\u0930\u094d\u0915\u0916\u0916'
                                r'\u093c\u0916\u094d\u092f\u0916\u094d\u092e\u0930\u094d\u0916\u0917\u0917'
                                r'\u094d\u0930\u0917\u094d\u092f\u0917\u094d\u092e\u0917\u094d\u0924\u0930'
                                r'\u094d\u0917\u0917\u0952\u095a\u0918\u0918\u094d\u0930\u0918\u094d\u092f'
                                r'\u0930\u094d\u0918\u091a\u091a\u094d\u0930\u091a\u094d\u091a\u091a\u094d'
                                r'\u092f\u091a\u094d\u091b\u0930\u094d\u091a\u091b\u091b\u094d\u0930\u0930'
                                r'\u094d\u091b\u091b\u0903\u091c\u091c\u094d\u0930\u0930\u094d\u091c\u091c'
                                r'\u093c\u091c\u0902\u091c\u094d\u092f\u091c\u0952\u0979\u091c\u094d\u0930'
                                r'\u095b\u091d\u091d\u094d\u092e\u091d\u094d\u0930\u0936\u0936\u094d\u0935'
                                r'\u0936\u094d\u0930\u0936\u094d\u091a\u0930\u094d\u0936\u0939\u0939\u094d'
                                r'\u0923\u0939\u094d\u0932\u0939\u094d\u0935\u0939\u094d\u092e\u0930\u094d'
                                r'\u0939\u0939\u094d\u092f\u0938\u0938\u094d\u0928\u0938\u094d\u0925\u0938'
                                r'\u094d\u091f\u0938\u094d\u091c\u0938\u094d\u0915\u0938\u094d\u0924\u0938'
                                r'\u094d\u0935\u0938\u094d\u0930\u0930\u094d\u0938\u0943\u0944\u0900\u094a'
                                r'\u097d\u094f\u0971\u093d\u25cc\u093a\u0954\u0970\u0953\u0957\u0952\u0956'
                                r'\u0903\u0946\u0943\u0944\u0900\u094a\u097d\u094f\u0971\u093d\u25cc\u093a'
                                r'\u0954\u0970\u0953\u0957\u0952\u0956\u0903\u0946\u091f\u091f\u094d\u091f'
                                r'\u0930\u094d\u091f\u091f\u094d\u0920\u091f\u094d\u0930\u091f\u0902\u0920'
                                r'\u0930\u094d\u0920\u0920\u094d\u0930\u0920\u0902\u0921\u0921\u0902\u0921'
                                r'\u093c\u0930\u094d\u0921\u095c\u0921\u0952\u0922\u0922\u0902\u0922\u093c'
                                r'\u0930\u094d\u0922\u095d\u0923\u0923\u094d\u0930\u0923\u094d\u0921\u0923'
                                r'\u094d\u091f\u0930\u094d\u0923\u0924\u0924\u094d\u0924\u0924\u094d\u0930'
                                r'\u0930\u094d\u0924\u0924\u094d\u092e\u0924\u094d\u0928\u0924\u094d\u0925'
                                r'\u0925\u0924\u094d\u0925\u0925\u094d\u0930\u0930\u094d\u0925\u0926\u0926'
                                r'\u094d\u0930\u0926\u094d\u0935\u0926\u094d\u0927\u0926\u094d\u0926\u0927'
                                r'\u0927\u094d\u0930\u0930\u094d\u0927\u0927\u094d\u0925\u0928\u0928\u094d'
                                r'\u0928\u0930\u094d\u0928\u0928\u094d\u092e\u0928\u094d\u0924\u0928\u094d'
                                r'\u092f\u0928\u093c\u0937\u0937\u0937\u094d\u091f\u0937\u094d\u0920\u0937'
                                r'\u094d\u005f\u0936\u094d\u0930\u0960\u0901\u0924\u094d\u0930\u091e\u0950'
                                r'\u091c\u094d\u091e\u093a\u050f\u0936\u094d\u0930\u0960\u0901\u0924\u094d'
                                r'\u0930\u091e\u0950\u091c\u094d\u091e\u093a\u092a\u092a\u094d\u092a\u0928'
                                r'\u094d\u092a\u092a\u094d\u092f\u092a\u094d\u0930\u0930\u094d\u092a\u092b'
                                r'\u092b\u093c\u092b\u0902\u0930\u094d\u092b\u092b\u094d\u0930\u092c\u092c'
                                r'\u094d\u092c\u092c\u094d\u0930\u0930\u094d\u092c\u092c\u0952\u092d\u092d'
                                r'\u094d\u0930\u092d\u094d\u092e\u0930\u094d\u092d\u092e\u0930\u094d\u092e'
                                r'\u092e\u094d\u0930\u092e\u0948\u0902\u092e\u094d\u092e\u092e\u094d\u0928'
                                r'\u092e\u094d\u092c\u092e\u094d\u0939\u092e\u0947\u0902\u092f\u092f\u094d'
                                r'\u0930\u0930\u094d\u092f\u092f\u093c\u097a\u0930\u0931\u0930\u0902\u0930'
                                r'\u094d\u0930\u0931\u0930\u094d\u0932\u0932\u094d\u0926\u0932\u094d\u092e'
                                r'\u0932\u094d\u0930\u0930\u094d\u0932\u090c\u0961\u0935\u0935\u094d\u092f'
                                r'\u0935\u094d\u0930\u0930\u094d\u0935\s]+')

# 保加利亚 bg
Bg_noCharacters = re.compile(r'[^у1е2и3ѝш4щ5к6с7д8з9ц0бьяаожгтнвмчюйъэфхпрл, .-:\'@#!,?УЕИЍШЩКСДЗЦБЬЯАОЖГТ'
                                r'НВМЧЮЙЪЭФХПРЛ¹½⅓¼⅛1²⅔2³⅜¾34⁴5⅝67⅞89ⁿ∅@#¢€£¥₱$%‰&_—–·\-+±(<{[)\]>/†★‡*”„“«»"\''
                                r'‚‘’‹›:¡!¿?_, ….~`|♪♣♠♥♦√πΠ÷×§¶∆£€¥¢←↑↓→^°′″=∞≠≈{},\©®™℅\[\]≤‹«<>›≥» ….\s]+')

# 孟加拉 bn
Bn_noCharacters = re.compile(r'[^\u09e7\u0999\u09e7\u09e8\u099e\u09e8\u09e9\u09a1\u09bc\u09e9\u09ea\u09a2\u09bc'
                             r'\u09ea\u09eb\u09af\u09bc\u09eb\u09ec\u09ce\u09ec\u09ed\u09b8\u09ed\u09ee\u0983\u09ee'
                             r'\u09ef\u0981\u09ef\u09e6\u0982\u09e6\u09e7\u0999\u09e7\u09e8\u099e\u09e8\u09e9\u09a1'
                             r'\u09bc\u09e9\u09ea\u09a2\u09bc\u09ea\u09eb\u09af\u09bc\u09eb\u09ec\u09ce\u09ec\u09ed'
                             r'\u09b8\u09ed\u0983\u0981\u0982\u09be\u09be\u09bf\u09bf\u09c0\u09c0\u09c1\u09c1\u09c2'
                             r'\u09c2\u09c7\u09c7\u09c8\u09c8\u09cb\u09cb\u09d7\u09d7\u09cc\u09cc\u09e7\u0985\u09e7'
                             r'\u09be\u09e8\u0986\u09e8\u09bf\u09e9\u0987\u09e9\u09c0\u09ea\u0988\u09ea\u09c1\u09eb'
                             r'\u0989\u09eb\u09c2\u09ec\u098a\u09ec\u09c7\u09ed\u098f\u09ed\u09c8\u09ee\u0990\u09ee'
                             r'\u09c4\u09c3\u098c\u098b\u09e1\u09e0\u09e2\u09e3\u09cd\u09ae\u09b8\u09a7\u09b0\u09ac'
                             r'\u099c\u099d\u09b6\u09b2\u09b7\u09a4\u099f\u09a0\u0995\u09af\u0996\u0997\u0998\u09a8'
                             r'\u099a\u099b\u20b9\u09bc\u09f0\u09f1\u09f2\u09f3\u09f4\u09f5\u09f7\u007c\u099f\u09cd'
                             r'\u09ae\u09ac\u09b0\u09a0\u09af\u09a1\u09a2\u09a3\u09a4\u09a5\u09a8\u09a6\u09a7\u09ad'
                             r'\u09b8\u09f9\u09fb\u09bd\u0980\u09f8\u09f6\u09fa\u002b\u09aa\u09cd\u099f\u09a4\u09a8'
                             r'\u09ae\u09b0\u09b2\u09ab\u09ac\u09a6\u09a7\u09af\u09ad\u0995\u0997\u09b9\u200c\u200d'
                             r'1234567890⅓¼⅛¹½১২²⅔৩¾³⅜৪⁴⅝৫৬⅞৭৮৯০∅ⁿ@#$$₱€¢£₹%‰&\-—_–·+±(<{[)}>)/★†‡*"„“”«»\'‚‘’‹›:'
                             r';¡!?¿_, .…~`|♣♠♪♥♦√πΠ÷×§¶∆£€¥¢$←↑↓→^°′″=∞≠≈{},\©®™℅[\]‹≤≤<>»≥› ….…\-:\'@#!,.?\s]+')

# 塞尔维亚 sr
Sr_noCharacters = re.compile(r'[^љ1њ2е3ѐр4т5з6у7и8ѝо9п0шасдфгхјклчћѕџцвбнмђж,. -:\'@#!,?ЀЍ¹½⅓¼⅛12²⅔3⅜³¾4⁴5⅝6⅞ⁿ∅ЉЊЕР'
                             r'ТЗУИОПШАСДФГХЈКЛЧЋЅЏЦВБНМЂЖ@#$€¢£¥₱%‰&-—_–·+±(<{[)\]}>/*★†‡"”„““»«\'’‚‘›‹:;!¡?¿_,.~`|'
                             r'•♣♠♪♥♦√Ππ÷×¶§∆£€¥¢^←↑↓→°′″=∞≠≈{},\©®™℅[\]‹≤«<>›≥»…\s]+')

# 希伯来 iw
Iw_noCharacters = re.compile(r'[^\u05E7\u05E8\u05D0\u05D8\u05D5\u05DF\u05DD\u05E4\u0030\u0031\u0032\u0033\u0034\u0035'
                             r'\u0036\u0037\u0038\u0039\u0027\u0022\u05E9\u05D3\u05D2\u05D2\u05F3\u05DB\u05E2\u05D9'
                             r'\u05F2\u05B7\u05D7\u05D7\u05F3\u05DC\u05DA\u05E3\u05D6\u05D6\u05F3\u05E1\u05D1\u05D4'
                             r'\u05E0\u05DE\u05E6\u05E6\u05F3\u05EA\u05EA\u05F3\u05E5\u05E5\u05F3¹½⅓¼⅛12²⅔3³⅜¾4⁴5⅝6⅞'
                             r'789∅ⁿ0@#€¢£¥₱$‰%&—_–·±﬩+>}\])(\[{</★*“”„»«"\'‘’‚›‹:;¡!¿?_!, .?~`|♣♠♪♥♦•√πΠ÷×§¶∆£€¥¢$↑←↓→'
                             r'^′″°≠∞≈=}{!,\\©®™℅\]\[›≥»><«≤‹ ?.\-:\'@#!,?\s]+')


# 希腊 el
El_noCharacters = re.compile(r'[^;1:ς2ε3έρ4τ5υϋ6ύύθ7ιΐϊ8ίοό9π0αάσδφγηήξκλζχψωώβνμ, .…¹½⅓¼⅛12²⅔3⅜³¾4⁴5⅝6⅞ⁿ∅;ςΕΡΤΥΘΙΟΠΑΣ'
                             r'ΔΦΓΗΞΚΛΖΧΨΩΒΝΜ1:;ςΕΈΡΤΥΫΎΫ́ΘΙΪ́ΪΊΟΌΠΑΆΣΔΦΓΗΉΞΚΛΖΧΨΩΏΒΝΜ@#$¢£¥₱€‰%&—_–·\-±+<{[)>\]}/*★†‡„“”'
                             r'«»‚‘’‹›:;¡!"\'¿?_~`|♣♠♪♥♦•√πΠ÷×§¶∆£¥$¢←↑↓→^′″°∞≠≈={},\©®™℅\[\]‹≤«›≥»<>.\s]+')

# 斯洛伐克 sk
Sk_noCharacters = re.compile(r'[^q1w2eèêëęěéēė3r4řŕŗtţ5ťyÿ6ýuûųùűūů7úüiıïìîįī8íoøőœõòöóô90paáåæąáäāàâsśšßşdďfgģğhjķkľĺļ'
                             r'łlźžżzxćčçcvbńñňņńm, .QWÈÊËĘĚÉĒĖEŘŔŖRŢŤTŸÝYÛŲÙŰŪŮÚÜUIÏÌÎĮĪÍIØŐŒÕÒÖÓÔ9OPÃÅÆĄÁÄĀÀÂAŚŠSSŞSĎ'
                             r'DFĢĞGHJĶKŁĻĹĽLŹŽŻZXĆČÇCVBÑÑŇŅŃNM@#$¢£¥₱€‰%&—_–·\-±+<{[(\]}>\)/★†‡*”„“»«"\'’‚‘›‹:;¡!¿?_, '
                             r'….~`|♣♠♪♥♦√πΠ÷×§¶∆£¥$¢←↑↓→^′″°∞≠≈={},\©®™℅[\]‹≤«›≥»<> .…¹½⅓¼⅛12²⅔3⅜³¾4⁴5⅝6⅞ⁿ∅\s]+')

# 阿塞拜疆  az
Az_noCharacters = re.compile(r'[^1q2ü3e4r5t6y7u8i9o0pöğəılkjhgfdsazxcvbnmçşQÜERTYUİOPÖĞƏILKJHGFDSAZXCVBNMÇŞ1234567890¹'
                             r'½⅓¼⅛²⅔³⅜¾⁴⅝⅞/\]\)}>({[<±+_\-—–·&‰%¢$€£¥₱#@†*★‡”"„“«»’\'‘‚‹›:;¡!¿?_,…~`|♪♠♣♥♦√πΠ÷×§¶∆,}{'
                             r'≠=≈∞′°″↑^←↓→¢¥€£\©®™℅[\]≥>»≤‹«\s]+')
# et_EE_拉脱维亚
Et_EE_noCharacters = re.compile(r'[^q1w2e3êëęěėēèérř4ŗŕtť5ţyÿ6ýuůûüűúų7ūùiıïíîìį8īoøőœöõôóò9p0aäåæąāàáâãsśšßşdďfgģğhjķ'
                                r'kļłĺľlzźžżxčćçcvbnńņñńm, .\-:\'@#!,?QWEÊËĘĚĖĒÈÉRŘŖŔTŤŢYŸÝUŮÛÜŰÚŲŪÙIIÏÍÎÌĮĪOØŐŒÖÕÔÓÒPA'
                                r'ÄÅÆĄĀÀÁÂÃASŚŠSSŞDĎFGĢĞHJKĶLĽĹŁĻZŹŽŻXCĆČÇVBNŃŅÑŃM, \-:\'@#!,?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞\ⁿ∅@#€¢£¥₱$%‰&'
                                r'\-—_–·+±(<{[)>}\]/★†‡*"”„“«»"\'’‚‘‹›:¡!¿?_ ….~`|♣♠♪♥♦√πΠ÷×§¶∆£€¥¢←↑↓→\^°′″=∞≠≈{},\©®™℅\['
                                r'\]‹≤«<>›≥» .…\s]+')

# 古吉拉特 gu
Gu_noCharacters = re.compile(r'[^\u0a99\u0a9e\u0aa3\u0ab3\u0a8b\u0ae0\u0abd\u0ad0\u0ac5\u0a8d\u0ac5\u0ac9\u0a91\u0ac9\u0a99'
                             r'\u0a9e\u0aa3\u0ab3\u0a8b\u0ae0\u0abd\u0ad0\u0a8d\u0ac5\u0a8d\u0a91\u0ac9\u0a91\u0acd\u0ae7'
                             r'\u0ac7\u0ABE\u0a86\u0ABE\u0ABF\u0a87\u0ABF\u0AC0\u0a88\u0AC0\u0AC1\u0a89\u0AC1\u0AC2\u0a8a'
                             r'\u0AC2\u0AC7\u0a8f\u0AC7\u0AC8\u0a00\u0AC8\u0ACB\u0a93\u0ACB\u0ACC\u0a94\u0ACC\u0ae7\u0a85'
                             r'\u0ae7\u0ac7\u0ae8\u0a86\u0ae8\u0ae9\u0a87\u0ae9\u0aea\u0a88\u0aea\u0aeb\u0a89\u0aeb\u0aec'
                             r'\u0a8a\u0aec\u0aed\u0a8f\u0aed\u0aee\u0a90\u0aee\u0aef\u0a93\u0aef\u0ae6\u0a94\u0ae6\u0a83'
                             r'\u0a82\u0ac3\u0ac4\u0ae1\u0ae2\u0ae3\u0a8c\u0abc\u0ac7\u0a81\u0a83\u0a82\u0ac3\u0ac4\u0ae1'
                             r'\u0ae2\u0ae3\u0a8c\u0abc\u0ac7\u0a81\u0a95\u0a95\u0acd\u0ab0\u0a95\u0acd\u0a95\u0a96\u0a96'
                             r'\u0acd\u0a96\u0a96\u0acd\u0ab0\u0a97\u0a97\u0acd\u0a95\u0a97\u0acd\u0a97\u0a97\u0acd\u0ab0'
                             r'\u0a98\u0a98\u0acd\u0aaf\u0a98\u0acd\u0ab5\u0a98\u0acd\u0ab0\u0a9a\u0a9a\u0acd\u0a95\u0a9b'
                             r'\u0a9c\u0a9c\u0acd\u0aaf\u0a9c\u0acd\u0ab0\u0a9d\u0ab6\u0ab6\u0acd\u0aae\u0ab6\u0acd\u0ab0'
                             r'\u0ab6\u0acd\u0aa8\u0ab6\u0acd\u0ab5\u0ab7\u0ab7\u0acd\u0a9f\u0ab7\u0acd\u0a95\u0ab0\u0acd'
                             r'\u0ab7\u0ab8\u0ab8\u0acd\u0ab2\u0ab8\u0acd\u0ab5\u0ab8\u0acd\u0aae\u0ab8\u0acd\u0aa4\u0af0'
                             r'\u0a95\u0acd\u0ab7\u0a9c\u0acd\u0a9e\u0aa4\u0acd\u0ab0\u20b9\u0af1\u0021\u0023\u003f\u0026'
                             r'\u003a\u0af0\u0a95\u0acd\u0ab7\u0a9c\u0acd\u0a9e\u0aa4\u0acd\u0ab0\u20b9\u0af1\u0021\u0023'
                             r'\u003f\u0026\u003a\u0a9f\u0a9f\u0acd\u0ab0\u0a9f\u0acd\u0a9f\u0aa0\u0aa0\u0acd\u0aa0\u0aa1'
                             r'\u0aa1\u0acd\u0aa1\u0aa1\u0acd\u0aa8\u0aa2\u0aa2\u0acd\u0ab5\u0aa2\u0acd\u0aa2\u0aa2\u0acd'
                             r'\u0ab0\u0aa4\u0aa4\u0acd\u0ab0\u0aa4\u0acd\u0a95\u0aa4\u0acd\u0aa4\u0aa4\u0acd\u0a95\u0aa5'
                             r'\u0aa5\u0acd\u0aa5\u0aa6\u0aa6\u0acd\u0ab0\u0aa6\u0acd\u0aa7\u0aa6\u0acd\u0aae\u0aa7\u0aa7'
                             r'\u0acd\u0aaf\u0aa7\u0acd\u0ab5\u0aa7\u0acd\u0a98\u0aa8\u0aa8\u0acd\u0a95\u0aa8\u0acd\u0aa4'
                             r'\u0aa8\u0acd\u0ab8\u0ab9\u0ab9\u0acd\u0ab0\u0ab9\u0acd\u0aaf\u0ab9\u0acd\u0aae\u0aa1\u0040'
                             r'\u007c\u0024\u005f\u007c\u007c\\u002d\u002b\u002f\u003b\u0040\u0023\u0024\u005f\u007c\u007c'
                             r'\\u002d\u002b\u002f\u003b\u0aaa\u0aaa\u0acd\u0a95\u0aaa\u0acd\u0ab0\u0aaa\u0acd\u0aaf\u0aab'
                             r'\u0aac\u0aac\u0acd\u0a95\u0aac\u0acd\u0ab0\u0aac\u0acd\u0aac\u0aad\u0aad\u0acd\u0a95\u0aae'
                             r'\u0aae\u0acd\u0a95\u0aae\u0acd\u0a9b\u0aae\u0acd\u0aa4\u0aae\u0acd\u0ab0\u0aae\u0acd\u0aae'
                             r'\u0aaf\u0aaf\u0acd\u0a95\u0ab0\u0ab0\u0acd\u0a95\u0ab0\u0acd\u0ab0\u0ab0\u0acd\u0aa4\u0ab2'
                             r'u0ab2\u0acd\u0ab2\u0ab2\u0acd\u0a95\u0ab2\u0acd\u0ab0\u0ab5\u0ab5\u0acd\u0ab0\u0ab5\u0acd'
                             r'\u0aaf1234567890¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞/\])}>({[<±+_\-—–·&‰%¢$€£¥₱#@†*★‡”"„“«»’\'‘‚‹›:;¡!¿?_,…~`|♪♠♣'
                             r'♥♦√πΠ÷×§¶∆,}{≠=≈∞′°″↑^←↓→¢¥€£\©®™℅[\]≥>»≤‹«\s]+')

# hr_克罗地亚
Hr_noCharacters = re.compile(r'[^q1w2e3r4t5z6źžżu7i8o9p0asßšśdđfghjklyxcčçćvbnñńm, .-:\'@#!,?QWERTZŹŽŻUIOPASSSŠŚDĐFGHJKLY'
                             r'XCČÇĆVBNÑŃM¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#€¢£¥₱‰%$&_—–·\-±+<{[\]}>\)(/★†‡*“„”»«"\'‘‚’›‹:;¡!¿?_,….~`|♪♣♠♥'
                             r'♦•√πΠ÷×§¶∆£€¥¢←↑↓→^′″°≠≈∞={},\©®™℅[\]≤‹«<>›≥» .…\s]+')


# in_印度尼西亚
In_noCharacters = re.compile(r'[^q1w2e3r4t5y6u7i8o9p0lkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM/\])}>{([<+±\-_—–·&‰%¢$€£¥₱#'
                             r'@†*★‡”"“„«»’\'‘‚‹›:;¡!¿?….~`|♪•♥♦♣♠√πΠ÷×§¶∆,}{≠=≈∞′°″↑^←↓→¢¥€£\©®™℅[\]≥>»›≤<«‹\s]+')

# pt_BR 西葡萄语
Pt_BR_noCharacters = re.compile(r'[^12qw3eêéèëėęēr45t6y7uúüûùū8iíîìįïīo9óõôòöœøōºp0lkjhgfdsáaãàâªæåäzxçcčćxvbnmQWEÊÉÈËĖĘĒRTYUÚÜ'
                             r'ÛÙŪIÍI8ÎÌĮÏĪOÓÕÔÒÖŒØŌºPLKJHGFDSÁAÃÀÂÄÅÆªZXÇCČĆVBNM¹½⅓¼⅛²#⅔⁴⅝⅞ⁿ∅/\])}>({<[±+_\-–·—&‰%¢$€£¥₱#@†'
                             r'*★‡”"“„«»”’\'‘‚‹›:;¡!¿?….,_~`|♪•♥♦♠♣√πΠ÷×§¶∆,}{≠=≈∞′°″↑^←↓→¢¥€£\©®™℅[\]≥>»›≤<‹«\s]+')

# ka_GE 格鲁吉亚
Ka_GE_noCharacters = re.compile(r'[^ქ1წ2ე3ჱრ4ტ5ყ6ჸუ7ი8ჲო9პ0აჺსდჶფჹგჵჰჷჯკლზჴხცჳვბჼნმ, ,\-:\'@#!?.QჭEღთYUIOPAშDFGHჟKLძXჩVBNM¹½⅓'
                                r'¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#€¢£¥₱$%‰&_—–·\-+±(<{[)\]}>/*★†‡"”„“«»\'’‚‘‹›:;!¡?¿_, ….~`|♣♠♪♥♦•√πΠ÷×§¶∆£€¥¢←'
                                r'↑↓→^′″°≠∞≈={},\©®™℅[\]‹≤«<>›≥» ….\s]+')

# lt_立陶宛
Lt_noCharacters = re.compile(r'[^q1w2e3éêëěęėēèrř4ŗŕtť5ţyÿ6ýuűûùúůūų7ūüiıïíîìī8įoøőœôóòõö90pâãåæąäāàáasśšßşdďfgģğhjkķlľĺłļzźž'
                             r'żxčcćçvbnńņñńm, .\-:\'@#!,?QWEÉÊËĚĘĖĒÈRŘŖŔTŤŢYŸÝUŰÛÙÚŮŪŲŪÜIIÏÍÎÌĪĮOØŐŒÔÓÒÕÖPAÂÃÅÆĄÄĀÀÁŚŠSSŞSDĎF'
                             r'GĢĞHJKĶLĽĹŁĻZŹŽŻXCĆČÇVBNŃŅÑŃM, .\-:\'@#!,?¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅@#€¢£¥₱$%‰&\-—_–·+±({<[)>}\]/*†★‡”„“«»'
                             r'"\'’‚‘‹›:;¡!¿?_, .,…~`|♣♠♪♥♦√πΠ÷×§¶∆£€¥¢←↑↓→^′″°≠∞≈={},\©®™℅[\]‹≤«<>›≥» .…\s]+')

# lv_拉脱维亚
Lv_noCharacters = re.compile(r'[^q1w2e3êëęěėēèérř4ŗŕtť5ţyÿ6ýuůûüűúų7ūùiıïíîìį8īoøőœöõôóò9p0aäåæąāàáâãsśšßşdďfgģğhjķkļłĺľlzźžżx'
                             r'čćçcvbnńņñńm, .-:\'@#!,?QWEÊËĘĚĖĒÈÉRŘŖŔTŤŢYŸÝUŮÛÜŰÚŲŪÙIIÏÍÎÌĮĪOØŐŒÖÕÔÓÒPAÄÅÆĄĀÀÁÂÃASŚŠSSŞDĎFGĢĞ'
                             r'HJKĶLĽĹŁĻZŹŽŻXCĆČÇVBNŃŅÑŃM, -:\'@#!,?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#€¢£¥₱$%‰&\-—_–·+±(<{[)>}\]/★†‡*"”„“«»"\'’'
                             r'‚‘‹›:¡!¿?_ ….~`|♣♠♪♥♦√πΠ÷×§¶∆£€¥¢←↑↓→^°′″=∞≠≈{},\©®™℅[\]‹≤«<>›≥» .…\s]+')

# sl_斯诺文尼亚
Sl_noCharacters = re.compile(r'[^q1w2e3r4t5y6u7i8o9p0ašsđdfghjklžzxčćcvbnm, -:\'@#!,?. QWERTYUIOPASŠDĐFGHJKLZŽXCČĆVBNM¹½⅓¼⅛²⅔⅜'
                             r'³¾⁴⅝⅞ⁿ∅@#$¢£¥₱‰%€&_—–·\-±+<{[(\]}>)/★†‡*”„“»«"\'’‚‘›‹:;!¡?¿_, ….~`|♣♠♪♥♦√πΠ÷×§¶∆£¢$£←↑↓→^′″°∞≠≈='
                             r'{},\©®™℅[\]‹≤«≥›»<> ….\s]+')

# am_阿姆哈拉
Am_noCharacters = re.compile(r'[^\u1250\u1255\u1251\u1252\u1256\u1253\u1254\u125c\u1258\u125b\u125a\u12c8\u12c9\u12ca\u12cb\u12cc'
                             r'\u12cd\u12ce\u12cf\u1228\u1229\u122a\u122b\u122c\u122d\u122e\u122f\u1320\u1321\u1322\u1323\u1324\u1325'
                             r'\u1326\u1327\u12e8\u12e9\u12ea\u12eb\u12ec\u12ed\u12ee\u12ef\u1350\u1351\u1352\u1353\u1354\u1355\u1356'
                             r'\u1357\u138e\u138c\u138d\u138f\u1330\u1331\u1332\u1333\u1334\u1335\u1336\u1337\u1240\u1241\u1242\u1243'
                             r'\u1244\u1245\u1246\u124b\u124c\u1248\u124a\u124d\u12c8\u12c9\u12ca\u12cb\u12cc\u12cd\u12ce\u12cf\u1228'
                             r'\u1229\u122a\u122b\u122c\u122d\u122e\u122f\u1270\u1271\u1272\u1273\u1274\u1275\u1276\u1277\u12e8\u12e9'
                             r'\u12ea\u12eb\u12ec\u12ed\u12ee\u12ef\u1350\u1351\u1352\u1353\u1354\u1355\u1356\u1357\u138e\u138c\u138d'
                             r'\u138f\u1330\u1331\u1332\u1333\u1334\u1335\u1336\u1337\u1220\u1221\u1222\u1223\u1224\u1225\u1226\u1227'
                             r'\u12f8\u12f1\u12f2\u12f3\u12f4\u12f5\u12f6\u12f7\u1348\u1349\u134a\u134b\u134c\u134d\u134e\u134f\u138a'
                             r'\u1388\u1389\u138b\u1318\u131d\u1319\u131a\u131e\u131b\u131c\u2d95\u2d93\u2d94\u2d96\u131f\u1210\u1211'
                             r'\u1212\u1213\u1214\u1215\u1216\u1217\u1280\u1281\u1282\u1283\u1284\u1285\u1286\u128b\u128c\u1288\u128a'
                             r'\u128d\u12b8\u12b9\u12ba\u12bb\u12bc\u12bd\u12be\u12c3\u12c4\u12c0\u12c2\u12c5\u1340\u1341\u1342\u1343'
                             r'\u1344\u1345\u1346\u1347\u1338\u1339\u133a\u133b\u133c\u133d\u133e\u133f\u1230\u1231\u1232\u1233\u1234'
                             r'\u1235\u1236\u1237\u12f0\u12f1\u12f2\u12f3\u12f4\u12f5\u12f6\u12f7\u1348\u1349\u134a\u134b\u134c\u134d'
                             r'\u134e\u134f\u138a\u1388\u1389\u138b\u1308\u1309\u130a\u130b\u130c\u130d\u130e\u1313\u1314\u1310\u1312'
                             r'\u1315\u1200\u1201\u1202\u1203\u1204\u1205\u1206\u1207\u1300\u1301\u1302\u1303\u1304\u1305\u1306\u1307'
                             r'\u12a8\u12a9\u12aa\u12ab\u12ac\u12ad\u12ae\u12b3\u12b4\u12b0\u12b2\u12b5\u1208\u1209\u120a\u120b\u120c'
                             r'\u120d\u120e\u120f\u1340\u1341\u1342\u1343\u1344\u1345\u1346\u1347\u12e0\u12e1\u12e2\u12e3\u12e4\u12e5'
                             r'\u12e6\u12e7\u12d0\u12d1\u12d2\u12d3\u12d4\u12d5\u12d6\u1278\u1279\u127a\u127b\u127c\u127d\u127e\u127f'
                             r'\u1268\u1269\u126a\u126b\u126c\u126d\u126e\u126f\u1260\u1261\u1262\u1263\u1264\u1265\u1266\u1267\u1384'
                             r'\u1386\u1385\u1387\u1290\u1291\u1292\u1293\u1297\u1295\u1296\u1297\u1294\u1218\u1219\u121a\u121b\u121c'
                             r'\u121d\u121e\u121f\u1382\u1380\u1381\u1383\u1298\u1299\u129a\u129b\u129c\u129d\u129e\u129f\u12d8\u12d9'
                             r'\u12da\u12db\u12dc\u12dd\u12de\u12df\u12a0\u12a1\u12a2\u12a3\u12a4\u12a5\u12a6\u12a7\u1328\u1329\u132a'
                             r'\u132b\u132c\u132d\u132e\u132f\u1238\u1239\u123a\u123b\u123c\u123d\u123e\u123f\u1260\u1261\u1262\u1263'
                             r'\u1264\u1265\u1266\u1267\u1384\u1386\u1385\u1387\u1290\u1291\u1292\u1293\u1297\u1295\u1296\u1297\u1294'
                             r'\u1218\u1219\u121a\u121b\u121c\u121d\u121e\u121f\u1382\u1380\u1381\u1383\u1298\u1299\u129a\u129b\u129c'
                             r'\u129d\u129e\u129f፩⅓¼⅛1¹½፪፳2²⅔፫³፴33⅜፬⁴፵4፭⅝፶5፮፷6፯⅞፸7፰፹8፱9፺፲∅ⁿ0፼፻@#€¢£¥₱‰%&$_—–·\-+±(<{{\]}>)/★†‡*„“”«'
                             r'»"„“”«»\'‚‘’’›":;¡!¿?_, .\-:\'@፥፦፧፨#!,?፡።፣፤ ~`|♣♠♪♥♦√πΠ÷×§¶∆£€¥¢←↑↓→^°′″=∞≠≈{},\©®™℅[\]‹≤«›≥» ….\s]+')

# lo_LA 老挝
Lo_LA_noCharacters = re.compile(r'[^\u0ED1\u0ED2\u0ED3\u0ED4\u0ECC\u0EBC\u0ED5\u0ED6\u0ED7\u0ED8\u0ED9\u0ECD\u0EC8\u0EA2\u0ED1\u0E9F'
                                r'\u0ED2\u0EC2\u0ED3\u0E96\u0ED4\u0EB8\u0EB9\u0E84\u0ED5\u0E95\u0ED6\u0E88\u0ED7\u0E82\u0ED8\u0E8A'
                                r'\u0ED9\u0ECD\u0EBB\u0EC9\u0ED0\u0EB3\u0EC9\u0EB4\u0EC9\u0EB5\u0EC9\u0EA3\u0EDC\u0EBD\u201D\u0EAB'
                                r'\u0EBC\u0EBB\u0EC4\u0ED0\u0EB3\u0E9E\u0EB0\u0EB4\u0EB5\u0EAE\u0E99\u0E8D\u0E9A\u0EA5\u0EB1\u0EC9'
                                r'\u0ECA\u0ECB\u201C\u0EB1\u0EAB\u0E81\u0E94\u0EC0\u0EC9\u0EC8\u0EB2\u0EAA\u0EA7\u0E87\u201C\u20AD'
                                r'\u0EAF\u0EB6\u0EC9\u0EB7\u0EC9\u0EC6\u0EDD\u0E9C\u0E9B\u0EC1\u0EAD\u0EB6\u0EB7\u0E97\u0EA1\u0EC3'
                                r'\u0E9D1234567890¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞/\])}>({[<±+_\-—–·&‰%¢$€£¥₱#@†*★‡”"„“«»’\'‘‚‹›:;¡!¿?_,…~`|♪♠♣♥♦√πΠ÷×§¶'
                                r'∆,}{≠=≈∞′°″↑^←↓→¢¥€£\©®™℅[\]≥>»≤‹«\s]+')

# km_KH 高棉
Km_KH_noCharacters = re.compile(r'[^\u200D\u17D7\u200C\u0022\u17D1\u17DB\u20AC\u17D6\u17CD\u17D9\u17D0\u17DA\u17CF\u00AB\u00BB\u17CC'
                                r'\u00D7\u17CE\u17E1\u17F1\u17E2\u17F2\u17E3\u17F3\u17E4\u17F4\u17E5\u17F5\u17E6\u17F6\u17E7\u17F7\u17E8'
                                r'\u17F8\u17E9\u17F9\u17E0\u17F0\u17A5\u17A6\u17B2\u17B1\u200c\u200d\u0024\u0025\u0028\u0029\u002a\u007b'
                                r'\u007d\u1788\u17DC\u17BA\u17DD\u17C2\u17AC\u17AB\u1791\u17BD\u17BC\u17B8\u17C5\u1797\u17BF\u17B0\u1786'
                                r'\u17B9\u17C1\u179A\u178F\u1799\u17BB\u17B7\u17C4\u1795\u17C0\u17AA\u17A7\u17B1\u17B3\u17A9\u17A8\u17B6'
                                r'\u17C6\u17C3\u178C\u1792\u17A2\u17C7\u17C8\u17C8\u1789\u1782\u179D\u17A1\u17C4\u17C7\u17C9\u17AF\u17B6'
                                r'\u179F\u178A\u1790\u1784\u17A0\u17D2\u1780\u179B\u17BE\u17CB\u17AE\u17AD\u17B0¹½⅓¼⅛1²⅔23⅜³¾4⁴5⅝67⅞890'
                                r'ⁿ∅@#₱€¥£៛¢$%‰&—_–·\-±+<{[()\]}>/*★†‡"„””«»"\'‚‘’‹›:;¡!¿?_, ….~`|♣♠♪♥♦√πΠ÷×§¶∆£€¥¢←↑↓→^′″°≠∞≈={},\©®™℅['
                                r'\]‹≤«›≥»<> ….-:\'@#!,?\s]+')

# si 僧伽罗语
Si_noCharacters = re.compile(r'[^\u0d9e\u0d95\u0dda\u0d9f\u0ddb\u0dac\u0ddc\u0d92\u0ddd\u0db3\u0dde\u0d86\u0ddf\u0d87\u0d88\u0da5\u0da4'
                             r'\u0df4\u0d8f\u0d9e\u0dda\u0d95\u0ddb\u0d9f\u0ddc\u0dac\u0ddd\u0d92\u0dde\u0db3\u0ddf\u0d86\u0d88\u0d87\u0da4'
                             r'\u0da5\u0d8f\u0df4\u0dd6\u0dd4\u0d8b\u0d85\u0dd1\u0dd0\u0d8d\u0dbb\u0d8e\u0d94\u0d91\u0dc1\u0dc4\u0db9\u0db8'
                             r'\u0dc2\u0dc3\u0db0\u0daf\u0da1\u0da0\u0dd4\u0dd6\u0d85\u0d8b\u0dd0\u0dd1\u0dbb\u0d8d\u0d8e\u0d91\u0d94\u0dc4'
                             r'\u0dc1\u0db8\u0db9\u0dc3\u0dc2\u0daf\u0db0\u0da0\u0da1\u0ddf\u0dca\u0dd3\u0dd2\u0dd8\u0dcf\u0df2\u0dc6\u0dd9'
                             r'\u0da8\u0da7\u0dca\u200d\u0dba\u0dba\u0dc5\u0dd4\u0dc0\u0dab\u0db1\u0d9b\u0d9a\u0dae\u0dad\u0dca\u0ddf\u0dd2'
                             r'\u0dd3\u0dcf\u0dd8\u0df2\u0dd9\u0dc6\u0da7\u0da8\u0dba\u0dca\u200d\u0dba\u0dc0\u0dc5\u0dd4\u0db1\u0dab\u0d9a'
                             r'\u0d9b\u0dad\u0dae\u0dca\u200d\u0dbb\u0d83\u0d82\u0da3\u0da2\u0daa\u0da9\u0d8a\u0d89\u0db7\u0db6\u0db5\u0db4'
                             r'\u0dc5\u0dbd\u0d9d\u0d9c\u0dca\u200d\u0dbb\u0d82\u0d83\u0da2\u0da3\u0da9\u0daa\u0d89\u0d8a\u0db6\u0db7\u0db4'
                             r'\u0db5\u0dbd\u0dc5\u0d9c\u0d9d¹½⅓¼⅛12²⅔3⅜³¾4⁴5⅝6⅞789∅ⁿ0@#$¥₱€¢£₹‰%&_—–·\-+±<{[()\]}>/★†‡„“”«»"\'‚‘’‹›:;¡!¿?_, '
                             r'….~`|♪♣♪♥♦√πΠ÷×§¶∆£€¥¢$↑↓←→^′″°≠∞≈{},\©®™℅[\]≤‹«≥>›» ….\s]+')

# mk 马其顿
Mk_noCharacters = re.compile(r'[^љ1њ2е3ѐр4т5ѕ6у7и8ѝо9п0шасдфгхјклчќзџцвбнмѓж,-:\'@#!,? ЉЊЕЀРТЅУИЍОПШАСДФГХЈКЛЧЌЗЏЦВБНМЃЖ¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ@#€¢£'
                             r'¥₱$%‰&-—_–·+±(<{[)\]}>/*★†‡"”„“«»\'’‚‘‹›:;¡!¿?_, ….~`|•♣♠♪♥♦√πΠ÷×§¶∆£€¥¢←↑↓→^′″°∞≠≈={},\©®™℅[\]‹≤«›≥» .…\s]+')

def getCharacterPattern(language):
    if language.startswith("en_US"):
        characterPattern = en_US_noCharacters
    elif language.startswith("en_GB"):
        characterPattern = en_GB_noCharacters
    elif language.startswith("es"):
        characterPattern = Spanish_noCharacters
    elif language.startswith("it"):
        characterPattern = Italian_noCharacters
    elif language.startswith("de"):
        characterPattern = German_noCharacters
    elif language.startswith("fr"):
        characterPattern = French_noCharacters
    elif language.startswith("pl"):
        characterPattern = Polish_noCharacters
    elif language.startswith("ru"):
        characterPattern = Russian_noCharacters
    elif language.startswith("ar"):
        characterPattern = Arabic_noCharacters
    elif language.startswith("nl"):
        characterPattern = Dutch_noCharacters
    elif language.startswith("cs"):
        characterPattern = Czech_noCharacters
    elif language.startswith("tr"):
        characterPattern = Turkish_noCharacters
    elif language.startswith("ur"):
        characterPattern = Urdu_noCharacters
    elif language.startswith("ro"):
        characterPattern = Romanian_noCharacters
    elif language.startswith("fa"):
        characterPattern = Farsi_noCharacters
    elif language.startswith("uk"):
        characterPattern = Ukrainian_noCharacters
    elif language.startswith("pt_PT"):
        characterPattern = EuropeanPortuguese_noCharacters
    elif language.startswith("ms_MY"):
        characterPattern = Malay_noCharacters
    elif language.startswith("tl"):
        characterPattern = Tagalog_noCharacters
    elif language.startswith("hu"):
        characterPattern = Hungarian_noCharacters
    elif language.startswith("th"):
        characterPattern = Thai_noCharacters
    elif language.startswith("fi"):
        characterPattern = Finnish_noCharacters
    elif language.startswith("vi"):
        characterPattern = Vietnamese_noCharacters
    elif language.startswith("sv"):
        characterPattern = Swedish_noCharacters
    elif language.startswith("kk"):
        characterPattern = Kazakh_noCharacters
    elif language.startswith("da"):
        characterPattern = Danish_noCharacters
    elif language.startswith("nb"):
        characterPattern = Norwegian_noCharacters
    elif language.startswith("hi"):
        characterPattern = India_noCharacters
    elif language.startswith("bg"):
        characterPattern = Bg_noCharacters
    elif language.startswith("bn"):
        characterPattern = Bn_noCharacters
    elif language.startswith("sr"):
        characterPattern = Sr_noCharacters
    elif language.startswith("sk"):
        characterPattern = Sk_noCharacters
    elif language.startswith("iw"):
        characterPattern = Iw_noCharacters
    elif language.startswith("el"):
        characterPattern = El_noCharacters
    elif language.startswith("az"):
        characterPattern = Az_noCharacters
    elif language.startswith("et_EE"):
        characterPattern = Et_EE_noCharacters
    elif language.startswith("gu"):
        characterPattern = Gu_noCharacters
    elif language.startswith("hr"):
        characterPattern = Hr_noCharacters
    elif language.startswith("in"):
        characterPattern = In_noCharacters
    elif language.startswith("ka_GE"):
        characterPattern = Ka_GE_noCharacters
    elif language.startswith("lt"):
        characterPattern = Lt_noCharacters
    elif language.startswith("lv"):
        characterPattern = Lv_noCharacters
    elif language.startswith("pt_BR"):
        characterPattern = Pt_BR_noCharacters
    elif language.startswith("sl"):
        characterPattern = Sl_noCharacters
    elif language.startswith("am"):
        characterPattern = Am_noCharacters
    elif language.startswith("lo_LA"):
        characterPattern = Lo_LA_noCharacters
    elif language.startswith("km_KH"):
        characterPattern = Km_KH_noCharacters
    elif language.startswith("si"):
        characterPattern = Si_noCharacters
    elif language.startswith("mk"):
        characterPattern = Mk_noCharacters
    return characterPattern



time_regex = r"(\d+) ?: ?(\d+)"
time_nospace_regex = r"(\d+):(\d+)"
line_regex = r"(\w+) ?- ?(\w+)"
line_nospace_regex = r"(\w+)-(\w+)"
non_bracket_part1 = r"([^\(\)]*)"
bracket_regex1 = non_bracket_part1 + r"\(" + non_bracket_part1 + r"\)" + non_bracket_part1

non_bracket_part2 = r"([^\{\}]*)"
bracket_regex2 = non_bracket_part2 + r"\{" + non_bracket_part2 + r"\}" + non_bracket_part2

non_bracket_part3 = r"([^\[\]]*)"
bracket_regex3 = non_bracket_part3 + r"\[" + non_bracket_part3 + r"\]" + non_bracket_part3

non_bracket_part4 = r"([^\<\>]*)"
bracket_regex4 = non_bracket_part4 + r"\<" + non_bracket_part4 + r"\>" + non_bracket_part4

non_bracket_part5 = r"([^\‹\›]*)"
bracket_regex5 = non_bracket_part5 + r"\‹" + non_bracket_part5 + r"\›" + non_bracket_part5

non_bracket_part6 = r"([^\«\»]*)"
bracket_regex6 = non_bracket_part6 + r"\«" + non_bracket_part6 + r"\»" + non_bracket_part6

non_bracket_part7 = r"([^\“\”]*)"
bracket_regex7 = non_bracket_part7 + r"\“" + non_bracket_part7 + r"\”" + non_bracket_part7

non_bracket_part8 = r"([^\‘\’]*)"
bracket_regex8 = non_bracket_part8 + r"\‘" + non_bracket_part8 + r"\’" + non_bracket_part8

non_bracket_part9 = r"([^\„\”]*)"
bracket_regex9 = non_bracket_part9 + r"\„" + non_bracket_part9 + r"\”" + non_bracket_part9

non_bracket_part10 = r"([^\¡\!]*)"
bracket_regex10 = non_bracket_part10 + r"\¡" + non_bracket_part10 + r"\!" + non_bracket_part10

non_bracket_part11 = r"([^\¿\?]*)"
bracket_regex11 = non_bracket_part11 + r"\¿" + non_bracket_part11 + r"\?" + non_bracket_part11

non_quote_part1 = r'([^"]*)'
quote_regex1 = non_quote_part1 + r'"' + non_quote_part1 + r'"' + non_quote_part1

non_quote_part2 = r'([^“]*)'
quote_regex2 = non_quote_part2 + r'“' + non_quote_part2 + r'“' + non_quote_part2

non_quote_part4 = r'([^”]*)'
quote_regex4 = non_quote_part4 + r'”' + non_quote_part4 + r'”' + non_quote_part4
non_quote_part3 = r'([^\']*)'
quote_regex3 = non_quote_part3 + r'\'' + non_quote_part3 + r'\'' + non_quote_part3

def replace_clock_time(line):
    # 删除时间表示中冒号左右的空格 12 : 31 --> 12:31
    return re.sub(time_regex, r"\1:\2", line)
def replace_line_time(line):
    # 删除时间表示中冒号左右的空格 12 : 31 --> 12:31
    return re.sub(line_regex, r"\1-\2", line)

def replace_clock_time_noSpace(line):
    # 增加时间表示中冒号左右的空格 12:31 --> 12 : 31
    return re.sub(time_nospace_regex, r"\1 : \2", line)


def replace_brackets_1(line):
    # 匹配有左右括号的句子，并删除空格  ( how are you ),she said. --> (how are you),she said.
    re_obj = re.fullmatch(bracket_regex1, line)
    if re_obj:
        return re_obj[1] + '(' + re_obj[2].strip() + ')' + re_obj[3]
    else:
        return line

def replace_brackets_2(line):
    # 匹配有左右括号的句子，并删除空格  { how are you },she said. --> {how are you},she said.
    re_obj = re.fullmatch(bracket_regex2, line)
    if re_obj:
        return re_obj[1] + '{' + re_obj[2].strip() + '}' + re_obj[3]
    else:
        return line
def replace_brackets_3(line):
    # 匹配有左右括号的句子，并删除空格  { how are you },she said. --> {how are you},she said.
    re_obj = re.fullmatch(bracket_regex3, line)
    if re_obj:
        return re_obj[1] + '[' + re_obj[2].strip() + ']' + re_obj[3]
    else:
        return line
def replace_brackets_4(line):
    # 匹配有左右括号的句子，并删除空格  { how are you },she said. --> {how are you},she said.
    re_obj = re.fullmatch(bracket_regex4, line)
    if re_obj:
        return re_obj[1] + '<' + re_obj[2].strip() + '>' + re_obj[3]
    else:
        return line
def replace_brackets_5(line):
    # 匹配有左右括号的句子，并删除空格  { how are you },she said. --> {how are you},she said.
    re_obj = re.fullmatch(bracket_regex5, line)
    if re_obj:
        return re_obj[1] + '‹' + re_obj[2].strip() + '›' + re_obj[3]
    else:
        return line
def replace_brackets_6(line):
    # 匹配有左右括号的句子，并删除空格  { how are you },she said. --> {how are you},she said.
    re_obj = re.fullmatch(bracket_regex6, line)
    if re_obj:
        return re_obj[1] + '«' + re_obj[2].strip() + '»' + re_obj[3]
    else:
        return line
def replace_brackets_7(line):
    # 匹配有左右括号的句子，并删除空格  { how are you },she said. --> {how are you},she said.
    re_obj = re.fullmatch(bracket_regex7, line)
    if re_obj:
        return re_obj[1] + '“' + re_obj[2].strip() + '”' + re_obj[3]
    else:
        return line
def replace_brackets_8(line):
    # 匹配有左右括号的句子，并删除空格  { how are you },she said. --> {how are you},she said.
    re_obj = re.fullmatch(bracket_regex8, line)
    if re_obj:
        return re_obj[1] + '‘' + re_obj[2].strip() + '’' + re_obj[3]
    else:
        return line
def replace_brackets_9(line):
    # 匹配有左右括号的句子，并删除空格  { how are you },she said. --> {how are you},she said.
    re_obj = re.fullmatch(bracket_regex9, line)
    if re_obj:
        return re_obj[1] + '„' + re_obj[2].strip() + '”' + re_obj[3]
    else:
        return line
def replace_brackets_10(line):
    # 匹配有左右括号的句子，并删除空格  { how are you },she said. --> {how are you},she said.
    re_obj = re.fullmatch(bracket_regex10, line)
    if re_obj:
        return re_obj[1] + '¡' + re_obj[2].strip() + '!' + re_obj[3]
    else:
        return line

def replace_brackets_11(line):
    # 匹配有左右括号的句子，并删除空格  { how are you },she said. --> {how are you},she said.
    re_obj = re.fullmatch(bracket_regex11, line)
    if re_obj:
        return re_obj[1] + '¿' + re_obj[2].strip() + '?' + re_obj[3]
    else:
        return line

def replace_brackets_noSpace(line):
    # 匹配有左右括号的句子，并增加空格  (how are you),she said. --> ( how are you ),she said.
    re_obj = re.fullmatch(bracket_regex1, line)
    if re_obj:
        return re_obj[1] + '( ' + re_obj[2].strip() + ' )' + re_obj[3]
    else:
        return line


def replace_quotes_1(line):
    # 匹配有两个双引号的句子，并删除空格  " how are you ",she said. --> "how are you",she said.
    re_obj = re.fullmatch(quote_regex1, line)
    if re_obj:
        return re_obj[1] + '"' + re_obj[2].strip() + '"' + re_obj[3]
    else:
        return line
def replace_quotes_2(line):
    # 匹配有两个双引号的句子，并删除空格  " how are you ",she said. --> "how are you",she said.
    re_obj = re.fullmatch(quote_regex2, line)
    if re_obj:
        return re_obj[1] + '”' + re_obj[2].strip() + '”' + re_obj[3]
    else:
        return line
def replace_quotes_3(line):
    # 匹配有两个双引号的句子，并删除空格  " how are you ",she said. --> "how are you",she said.
    re_obj = re.fullmatch(quote_regex3, line)
    if re_obj:
        return re_obj[1] + '\'' + re_obj[2].strip() + '\'' + re_obj[3]
    else:
        return line

def replace_quotes_4(line):
    # 匹配有两个双引号的句子，并删除空格  " how are you ",she said. --> "how are you",she said.
    re_obj = re.fullmatch(quote_regex4, line)
    if re_obj:
        return re_obj[1] + '”' + re_obj[2].strip() + '”' + re_obj[3]
    else:
        return line

def replace_quotes_noSpace(line):
    # 匹配有两个双引号的句子，并增加空格  "how are you",she said. --> " how are you ",she said.
    re_obj = re.fullmatch(quote_regex1, line)
    if re_obj:
        return re_obj[1] + '" ' + re_obj[2].strip() + ' "' + re_obj[3]
    else:
        return line


def test_re():

    text = "اه يا قلبي . . الله يصبرني عليه . . ان شاء الله انت بتس" \
           "	 الدنيا تبتسم لي شويه كده ، ، يوم أو إتنين بس ، ، بعدها تدديني علي دماغي ، ، جااااااامد" \
           "اعدني بالتفاهم معاه ، بالذات انه نفس برجك الجدي "
    text = text.strip().lower()
    pattern_ = Arabic_noCharacters
    # pattern_ = Urdu_Characters
    print(text)
    # tmp = re.sub(pattern_, "", text)
    # print(tmp)

    m = re.search(pattern_, text)
    all = re.findall(pattern_, text)

    if m:
        print("-" * 100)
        print("m:", m)
        print("all:", all)
        # print(text)
    else:
        print('not match')


    # print("....", "\ufeff", "u0x2e")

    character = "и"
    print("\u0438")  # и
    print(ord(character))  # 1080
    print(chr(ord(character) + 1))  # и
    print(ascii(character))  # Unicode
    print(hex(ord(character)))  # 十六进制:0x438
    print(oct(ord(character)))  # 八进制:0o2070


if __name__ == "__main__":
    test_re()
