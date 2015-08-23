#!/usr/bin/python

import getopt
import sys
import string
import os
import os.path

####################################
# English->galactic Dictionary
dict = {}

# galactic->English Dictionary
gdict = {}
nulang = ""
currlang = ""
phrase = "" #only set if an argument is passed.
verbose = 1 #default to printing extra info

################## SET filehome to location of .lng files
#filehome = "/home/joela/Dropbox/python/langs/" #default
filehome = "langs/" #default
def bajor():
            global currlang

            currlang = "bajor"
            dict["a"] = "kurb"
            dict["about"]= "wynevsa"
            dict["above"]= "elas"
            dict["absolute"]= "plek"
            dict["affected"]= "tnejl"
            dict["after"]= "ran"
            dict["again"]= "osamat"
            dict["all"]= "jtyh"
            dict["already"]= "sanajn"
            dict["also"]= "rolpyresnak"
            dict["always"]= "sme"
            dict["am"]= "sog"
            dict["and"]= "lonmago"
            dict["anew"]= "ratk"
            dict["anothen"]= "rprba"
            dict["answered"]= "twrao"
            dict["any"]= "llmosary"
            dict["are"]= "rele"
            dict["arose"]= "rribse"
            dict["arrival"]= "rajus"
            dict["as"]= "rocar"
            dict["ascended"]= "kupus"
            dict["assuredly"]= "asneer"
            dict["at"]= "prokr"
            dict["authority"]= "promly"
            dict["avoidance"]= "rureril"
            dict["balance"]= "netseb"
            dict["baptized"]= "katsodsas"
            dict["baptizes"]= "gnanr"
            dict["baptizing"]= "pratdu"
            dict["be"]= "nanpi"
            dict["because"]= "rbaal"
            dict["become"]= "lemd"
            dict["been"]= "satw"
            dict["before"]= "setit"
            dict["behold"]= "nekpal"
            dict["belief"]= "bmasr"
            dict["believe"]= "ektl"
            dict["believed"]= "pehet"
            dict["believes"]= "maddapo"
            dict["belongs"]= "ratakut"
            dict["better"]= "aslaj"
            dict["beyond"]= "nus"
            dict["blessed"]= "lahtatapad"
            dict["blows"]= "ravnwoma"
            dict["born"]= "rsaluc"
            dict["breath"]= "in"
            dict["bride"]= "spadn"
            dict["bridegroom"]= "brdasati"
            dict["brothers"]= "ites"
            dict["but"]= "mlb"
            dict["by"]= "svltypaneb"
            dict["came"]= "ipkot"
            dict["can"]= "hashara"
            dict["cause"]= "kunk"
            dict["change"]= "mako"
            dict["christ"]= "hdes"
            dict["come"]= "kysrovaton"
            dict["comes"]= "difvakeki"
            dict["coming"]= "mluek"
            dict["communicates"]= "ampen"
            dict["confrontation"]= "nyrloren"
            dict["conquers"]= "ntajut"
            dict["consequences"]= "rdunh"
            dict["constitutes"]= "rohkaj"
            dict["context"]= "jrad"
            dict["creator"]= "nlicava"
            dict["darkness"]= "srpag"
            dict["dead"]= "rab"
            dict["deception"]= "sablon"
            dict["decrease"]= "bemgi"
            dict["defines"]= "tunogt"
            dict["descended"]= "rnry"
            dict["didn"]= "ahseh"
            dict["die"]= "cavt"
            dict["dies"]= "nesk"
            dict["disbelieves"]= "nasos"
            dict["disciples"]= "sksi"
            dict["disobeys"]= "luer"
            dict["divine"]= "htok"
            dict["do"]= "amtoar"
            dict["does"]= "laah"
            dict["doesn"]= "lvad"
            dict["don"]= "amrs"
            dict["done"]= "pnsde"
            dict["dwelling"]= "acnas"
            dict["earth"]= "alik"
            dict["earthly"]= "kitg"
            dict["enemy"]= "gmke"
            dict["enon"]= "remarp"
            dict["enter"]= "larkanare"
            dict["era"]= "kyssdi"
            dict["eternal"]= "mrin"
            dict["eternity"]= "rbos"
            dict["even"]= "clmad"
            dict["ever"]= "hinah"
            dict["every"]= "bfa"
            dict["everyone"]= "rtlere"
            dict["evil"]= "donrocom"
            dict["exclusively"]= "wyrd"
            dict["existance"]= "sarsl"
            dict["existence"]= "yhsak"
            dict["exists"]= "rps"
            dict["experience"]= "delur"
            dict["exposed"]= "jmritikarok"
            dict["eyes"]= "sersehlo"
            dict["false"]= "dteram"
            dict["father"]= "lakn"
            dict["fear"]= "tadur"
            dict["flesh"]= "mydrabase"
            dict["fools"]= "lai"
            dict["for"]= "clal"
            dict["foreign"]= "bud"
            dict["friend"]= "janat"
            dict["from"]= "pphir"
            dict["full"]= "ratta"
            dict["gave"]= "prrim"
            dict["genocide"]= "lmnam"
            dict["given"]= "silnabatm"
            dict["gives"]= "herrn"
            dict["god"]= "sbelse"
            dict["gods"]= "unkat"
            dict["going"]= "lgkis"
            dict["greatly"]= "pipot"
            dict["greed"]= "enetak"
            dict["greek"]= "nalto"
            dict["guide"]= "dden"
            dict["hand"]= "hared"
            dict["has"]= "hesk"
            dict["hates"]= "racob"
            dict["have"]= "medlja"
            dict["he"]= "nbocf"
            dict["hear"]= "tekatr"
            dict["heard"]= "nmbreta"
            dict["hears"]= "salr"
            dict["heaven"]= "arlum"
            dict["heavenly"]= "rarap"
            dict["here"]= "mnra"
            dict["him"]= "saro"
            dict["his"]= "nara"
            dict["how"]= "tekraka"
            dict["i"]= "nahh"
            dict["ideas"]= "luo"
            dict["if"]= "nteb"
            dict["ignore"]= "ksapc"
            dict["immutability"]= "rts"
            dict["imperative"]= "porhl"
            dict["in"]= "mwu"
            dict["increase"]= "rnit"
            dict["inevitable"]= "laklnota"
            dict["into"]= "rutka"
            dict["is"]= "dekmah"
            dict["isn"]= "lejt"
            dict["israel"]= "remcu"
            dict["it"]= "nebtyrkanur"
            dict["its"]= "jahah"
            dict["jesus"]= "kinasma"
            dict["jews"]= "kyk"
            dict["john"]= "tpebk"
            dict["jordan"]= "nudar"
            dict["joy"]= "netdasylaht"
            dict["judea"]= "nrvet"
            dict["judge"]= "kanag"
            dict["judged"]= "ltohae"
            dict["judgment"]= "hervneto"
            dict["justfies"]= "enj"
            dict["justifies"]= "lapp"
            dict["kingdom"]= "lelkisebevyj"
            dict["know"]= "rtran"
            dict["land"]= "rarni"
            dict["language"]= "nech"
            dict["legands"]= "pjn"
            dict["lest"]= "goej"
            dict["lies"]= "radnalnam"
            dict["life"]= "tivet"
            dict["lifted"]= "adhan"
            dict["light"]= "ttamite"
            dict["listen"]= "pkak"
            dict["live"]= "rll"
            dict["look"]= "pe"
            dict["looking"]= "ehrir"
            dict["love"]= "slaht"
            dict["loved"]= "nadd"
            dict["loves"]= "sasnosatl"
            dict["made"]= "ijler"
            dict["man"]= "srro"
            dict["manner"]= "msys"
            dict["marvel"]= "ksgerim"
            dict["maturity"]= "rensevinas"
            dict["may"]= "knhamalk"
            dict["means"]= "poti"
            dict["measure"]= "kelsel"
            dict["men"]= "maskyparanar"
            dict["messiah"]= "mahlem"
            dict["messianic"]= "gekol"
            dict["mindedness"]= "panol"
            dict["moses"]= "nakkesagam"
            dict["most"]= "ufak"
            dict["mother"]= "temah"
            dict["movement"]= "nls"
            dict["much"]= "mtokaa"
            dict["must"]= "botm"
            dict["my"]= "najatr"
            dict["name"]= "nppaseda"
            dict["named"]= "farnaleleb"
            dict["near"]= "mbok"
            dict["never"]= "riral"
            dict["nicodemus"]= "mlelr"
            dict["night"]= "nirn"
            dict["no"]= "sadyson"
            dict["noncorporeality"]= "olelir"
            dict["nor"]= "utakon"
            dict["not"]= "dava"
            dict["note"]= "sashap"
            dict["nothing"]= "antah"
            dict["now"]= "risp"
            dict["occurrences"]= "navak"
            dict["of"]= "sakurep"
            dict["old"]= "ynlas"
            dict["omniscience"]= "jshin"
            dict["on"]= "rarat"
            dict["one"]= "cblakih"
            dict["only"]= "kura"
            dict["open"]= "hekabos"
            dict["or"]= "tysuk"
            dict["origin"]= "ralas"
            dict["our"]= "ssasha"
            dict["out"]= "dane"
            dict["over"]= "wravr"
            dict["own"]= "nysmalakas"
            dict["pagh"]= "ragtoh"
            dict["part"]= "dilpok"
            dict["people"]= "rnavah"
            dict["perfect"]= "hiha"
            dict["perish"]= "radk"
            dict["pharisees"]= "stev"
            dict["physical"]= "dajuhho"
            dict["pneuma"]= "ralt"
            dict["power"]= "avnn"
            dict["primary"]= "rlla"
            dict["priority"]= "bpa"
            dict["prison"]= "dua"
            dict["prophecy"]= "ranatl"
            dict["prophets"]= "weldec"
            dict["providence"]= "suntarute"
            dict["purification"]= "benla"
            dict["questioning"]= "njops"
            dict["rabbi"]= "skers"
            dict["rather"]= "dja"
            dict["receive"]= "tano"
            dict["received"]= "kitm"
            dict["receives"]= "kiol"
            dict["rejoices"]= "errab"
            dict["remains"]= "dadalel"
            dict["rest"]= "enmak"
            dict["resurrection"]= "litf"
            dict["retribution"]= "nevns"
            dict["revealed"]= "domu"
            dict["reveals"]= "resopro"
            dict["reward"]= "nbarar"
            dict["root"]= "lsurh"
            dict["ruler"]= "linpa"
            dict["s"]= "redra"
            dict["said"]= "naal"
            dict["salim"]= "sapekaw"
            dict["same"]= "waek"
            dict["saved"]= "tostsibu"
            dict["seal"]= "dwt"
            dict["second"]= "eratan"
            dict["see"]= "tatkk"
            dict["seen"]= "attah"
            dict["send"]= "rard"
            dict["sent"]= "vnosuso"
            dict["serpent"]= "keba"
            dict["set"]= "tksekaha"
            dict["should"]= "mahon"
            dict["signs"]= "rosod"
            dict["silence"]= "hlor"
            dict["so"]= "masor"
            dict["solutions"]= "ntemee"
            dict["some"]= "penti"
            dict["son"]= "kpbuti"
            dict["sound"]= "kahamup"
            dict["speak"]= "lsym"
            dict["speaks"]= "vjomk"
            dict["spirit"]= "rtesep"
            dict["stands"]= "tarhot"
            dict["stayed"]= "nhosnu"
            dict["such"]= "cahb"
            dict["supreme"]= "hubp"
            dict["t"]= "tivse"
            dict["teacher"]= "hnebis"
            dict["tell"]= "nihi"
            dict["testified"]= "tetreklc"
            dict["testifies"]= "esdaan"
            dict["testify"]= "ajtoh"
            dict["than"]= "pnov"
            dict["that"]= "rtkak"
            dict["the"]= "bbebiterah"
            dict["their"]= "yms"
            dict["them"]= "cavhbudet"
            dict["there"]= "ssavke"
            dict["therefore"]= "mrml"
            dict["these"]= "akap"
            dict["they"]= "rbakan"
            dict["things"]= "rhlt"
            dict["this"]= "hsjecnejis"
            dict["through"]= "rasnadni"
            dict["thrown"]= "jetha"
            dict["til"]= "nlar"
            dict["time"]= "irnos"
            dict["to"]= "stanuc"
            dict["told"]= "kasu"
            dict["torah"]= "legokah"
            dict["translated"]= "gpijara"
            dict["true"]= "panuhk"
            dict["truth"]= "whpna"
            dict["understand"]= "tuo"
            dict["unity"]= "pahe"
            dict["unknown"]= "nhnori"
            dict["unless"]= "barek"
            dict["unparalleled"]= "safkas"
            dict["up"]= "makysan"
            dict["us"]= "shalla"
            dict["voice"]= "nenraw"
            dict["walk"]= "nanj"
            dict["wants"]= "vams"
            dict["was"]= "gobba"
            dict["water"]= "tpan"
            dict["we"]= "alpoan"
            dict["were"]= "same"
            dict["what"]= "mobna"
            dict["when"]= "arkoed"
            dict["where"]= "ronka"
            dict["which"]= "ndi"
            dict["who"]= "npolat"
            dict["whoever"]= "syal"
            dict["whom"]= "sojrapaki"
            dict["wilderness"]= "mernir"
            dict["will"]= "samla"
            dict["wind"]= "atmaar"
            dict["wisdom"]= "atnn"
            dict["with"]= "vbresndd"
            dict["within"]= "bsapao"
            dict["without"]= "ahyb"
            dict["witness"]= "rush"
            dict["womb"]= "hbk"
            dict["won"]= "motoj"
            dict["word"]= "rasirs"
            dict["words"]= "kilsa"
            dict["works"]= "tcvol"
            dict["world"]= "habta"
            dict["worship"]= "puc"
            dict["would"]= "artak"
            dict["wrath"]= "tarra"
            dict["yet"]= "kakvo"
            dict["you"]= "vpm"
            dict["your"]= "psbesanasos"



def usage():
            print "Help information here."
            print "*help    - this report" 
            print "*pItlh   - end program"
            print "*dict - dump out the dictionary"
            print "*lang - what is the current language?"
            print "lang XXX - load xxx.lng from language file archive"
            print "ADD eng gal = add English word mapped to Galactic"
            print "WRITE LANG - saves LANG.lng to language directory"
            print
            print "Command line: "
            print "-h, --help  : usage"
            print "-l, --lang= : set language"
            print "-q : minimal output"
            print "--phrase= : translate phrase"
            print "--home= : specify home for .lng files"
            print
            print
            
def loadlang(language):
        global currlang
        currlang = language 
            
        language = filehome+language+".lng"
        if verbose == 1:
            print "loading "+language
        wcount = 0

        if os.path.isfile((language)):
            with open(language) as f:
                        try:
                                    for line in f:
                                                line = line.strip("\n");
                                                (key, val) = line.split('",')
                                                val = val.strip('"') #remove terminal "
                                                val = val.strip(' "')#remove initial ' "'
                                                dict[string.strip(key, '"')] = string.strip(val, '"')
                                                wcount += 1
                        except:

                                                                                                    # end of file
                                    
                                    f.close()
                                    
                        if verbose == 1:
                            print str(wcount) + " words read"

        else:
                    if verbose == 1:
                        print language + " not found"
                        print "building Bajoran vocabulary"
                    bajor()

        #build reverse dictionary

        for english in dict:
                    gdict[dict[english]] = english




#collect command line options

try:                                
        (opts, args) = getopt.getopt(sys.argv[1:], "qhl:d", ["help", "lang=","phrase=","home="])

        for opt, arg in opts: 
                    if opt in ("-h", "--help"):    
                                usage()                     
                                sys.exit()                  
                    elif opt in ("-l", "--lang"):
                                nulang = arg
                    elif opt in ("-p", "--phrase"):
                        phrase = arg
                    elif opt in ("-q"):
                        verbose = 0
                    elif opt in ("--home"):
                        filehome = arg

except getopt.GetoptError as err:
            usage()
            sys.exit(2)



if nulang == "":
            loadlang("tlhingan")

else:
            loadlang(nulang)

        
if verbose == 1:
    print "         UTA: Universal Translator Assistant"
    print "========================================================"
    print "I will map English <--> Galactic. Type '*pItlh' to end."
    print "                                        *help for usage."          
    print "--------------------------------------------------------"

while True:
    try:
        if phrase == "":
            inp =  raw_input('? ')
            
        else:
            inp=phrase
        
        trans = 1; # flag to clear if special actions
        inpx = inp.translate(string.maketrans("",""),"!#$%&()*+,-./:;<=>?@[\]^_{|}~)")
        a = inpx.split()

#######special cases

        if inp == "*help":
            usage()
            trans = 0 # special actions


        if inp == "*lang":
            print "current language:" + currlang
            a[0]=""
            trans = 0 # special actions

        if inp == "?":
            usage()
            trans = 0 # special actions
            a = ("help")


        if inp == "*pItlh":
                        break

        if inp == "*dict":
                    print  dict
                    trans = 0; # special actions
                    
        if a[0] == "lang":
                    dict = {}
                    gdict = {}
                    loadlang(a[1])
                    trans = 0 # special actions

        if a[0] == "ADD": 
                    dict[a[1]] = a[2]
                    gdict[a[2]] = a[1]
                    trans = 0 # special actions

        if a[0] == "WRITE":
                    ofile = open(filehome+a[1]+".lng",'w')
                    #ofile.write(dict)
                    #print dict
                    wcount = 0
                    for english in dict:
                                ofile.write('"'+english+'", '+'"'+dict[english]+'"\n')
                                wcount += 1

                    if verbose == 1:
                        print str(wcount) + " words saved"
                    ofile.close()
                    trans = 0 # special actions

### process input, if any
        outp = ""
        if a != ():
            for words in a:
                try:
                    outp = outp + " " + dict[words]
                                    
                except:
                    try:
                        outp = outp + " " + gdict[words]
                    except:
                        outp = outp + " " + "[" + words + "]"
                                        
            if trans == 1:
                    if verbose == 1:
                        print ">>> "+outp
                        print
                    else:
                        print outp
                        
                    if phrase != "":
                        break # end program
                        
    except:
        break
                
