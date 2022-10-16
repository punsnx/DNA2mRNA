import sys
print("****************************************************")
print("DNA Template Coverter Program")
print("This Program can convert the DNA Template to mRNA")
print("****************************************************")
print("*Required START & STOP Anti Codon,\nEx. TACTGCCGAATT (GET mRNA : AUGACGGCTUAA)")
print("****************************************************")
global dnabaseN
#INPUT HOW MUCH BASE ON DNA TEMPLATE?
while True:
  while True:
      try:
          dnabaseN = int(input("How many bases on the DNA Template :"))
          break
      except ValueError :
          print("[Not valid Type (string/float)]Please enter only intenger(Ex. 9,12,13,15,18,21)")
  if isinstance(dnabaseN, int):
      if dnabaseN < 9:
        print("[Number < 9]number must be >= 9")
      elif dnabaseN%3 != 0:
        print("[Number/3 not equal 0]number must devide 3 = 0")
      elif dnabaseN >= 9 & dnabaseN % 3 == 0:
          break
  else:
    print("Error unexpected")
    sys.exit()

global DNATem
global STOPCODON
#INPUT AND CHECK DNA TEMPLATE?
while True:
    # Check is String
    while True:
        try:
            DNATem = str(input("Enter DNA Template :"))
            break
        except ValueError:
            print("[Not valid Type (int/float)]Please enter only character(Ex. TACTGCCGAATT)")
    #Check is String
    if isinstance(DNATem, str):
        #Check is lowercase Character
        if DNATem.islower():
            print("Please enter only Uppercase character(Ex. TACTGCCGAATT)")
        elif ("U" in DNATem):
            print("DNA Template must not contain base U")
        #Check DNATem lengh != dnabaseN
        elif len(DNATem) != dnabaseN:
            print("DNA Template must have %d bases" % dnabaseN)
        #Check DNATem must start with START CODON (mRNA : AUG) (DNA : TAC)
        elif (not "T" in DNATem[0]) | (not "A" in DNATem[1]) | (not "C" in DNATem[2]):
            print("DNA Template must start with Anti START Codon [TAC] [GET mRNA: AUG]")

        # STOP CODON : (mRNA UAA UGA UAG) (DNA : ATT ACT ATC)
        elif ("A" in DNATem[-3]): # Char -3 = A (U)
            if ("T" in DNATem[-2]): # Char -2 = T (A)
                if ("T" in DNATem[-1]): # Char -1 = T (A)
                    STOPCODON = "UAA"
                    break
                elif ("C" in DNATem[-1]): # Char -1 = C (G)
                    STOPCODON = "UAG"
                    break
                else: # Char -1 != T/C (A/G)
                    print("DNA Template must end with Anti STOP Codon [ATT/ACT/ATC] [GET mRNA: UAA/UGA/UAG]")
            elif ("C" in DNATem[-2]): # Char -2 = C (G)
                if ("T" in DNATem[-1]) :# Char -1 = T (A)
                    STOPCODON = "UGA"
                    break
                else: # Char -1 != T (A)
                    print("DNA Template must end with Anti STOP Codon [ATT/ACT/ATC]")
            else: # Char -2 != T/C (A/G)
                print("DNA Template must end with STOP Anti STOP Codon [ATT/ACT/ATC]")
        elif (not "A" in DNATem[-3]): # Char -3 != A (U)
            print("DNA Template must end with Anti STOP Codon [ATT/ACT/ATC]")
    else:
        print("Error unexpected")
        sys.exit()

def changeDNABaseACGT():
    mRNACal = ""
    for i in range(0,(dnabaseN)):
        if "A" in DNATem[i]:
            mRNACal = mRNACal + "U"
        elif "C" in DNATem[i]:
            mRNACal = mRNACal + "G"
        elif "G" in DNATem[i]:
            mRNACal= mRNACal + "C"
        elif "T" in DNATem[i]:
            mRNACal = mRNACal + "A"
    return mRNACal

print("****************************************************")
print("mRNA :" + changeDNABaseACGT())
print("Start Codon : AUG")
print("Stop Codon : " + STOPCODON)
print("****************************************************")