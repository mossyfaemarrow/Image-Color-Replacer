from PIL import Image
import numpy as np
from blend_modes import multiply
import random

def hairRandomizer():
    colorList = ["FFFDEA","FFEFDC","D8D6CD","FFFFFF","D8D7D8",
                 "F1F3FF","E1DFFF","C8BECE","BBBABF","9D9D9F",
                 "808080","9494A9","545365","413C40","4D484F",
                 "636268","555555","4B4946","352C27","333333",
                 "1D2224","252A24","292B38","3A2E44","4C2A4F",
                 "6E235D","863290","724D79","8F7C8B","A794B2",
                 "E1CDFE","CCA4E0","9778BE","A261CF","DA4FFF",
                 "993BD1","7930B5","643F9C","580FC0","4D2C89",
                 "3F2B66","525195","757ADB","484AA1","2D237A",
                 "0D0A5B","212B5F","013485","1C51E7","324BA9",
                 "4866D5","2F83FF","6394DD","76A8FF","AEC8FF",
                 "7895C1","444F69","556979","2F4557","0D1E25",
                 "0B2D46","0A3D67","0086CE","2B768F","00B4D5",
                 "00FFF1","9AEAEF","72C4C4","3CA2A4","8DBCB4",
                 "E2FFE6","B2E2BD","9AFFC7","61AB89","148E67",
                 "005D48","1F483A","20603F","236825","1E361A",
                 "1E2716","425035","51684C","97AF8B","687F67",
                 "567C34","629C3F","7ECE73","9BFF9D","8ECE56",
                 "A5E32D","C6FF00","D1E572","E8FCB4","B4CD3D",
                 "A9A032","828335","697135","4B4420","7E7645",
                 "BEA55D","C18E1B","D1B300","FFE63B","F9E255",
                 "F7FF6F","FFEC80","EDE8B0","FDE9AC","FFD297",
                 "F6BF6C","E8AF49","D1B045","FFB53C","FA912B",
                 "FF8500","FFA147","FFB576","FF984F","D5602B",
                 "B2560D","B24407","FF5500","EF5C23","FF6841",
                 "FF7360","C15A39","C47149","B27749","C3996F",
                 "CABBA2","827A64","6D675B","564D48","766259",
                 "977B6C","774840","603E3D","57372C","301E1A",
                 "5A4534","72573A","855B33","91532A","8E5B3F",
                 "563012","7B3C1D","A44B28","8B3220","BA311C",
                 "E22D18","CE000D","AA0024","850012","581014",
                 "2D0102","451717","652127","8C272D","C1272D",
                 "DF3236","A12928","B13A3A","9A534D","CC6F6F",
                 "FEA0A0","EB799A","DB518D","E934AA","E7008B",
                 "8A024A","4D0F28","9C4975","E77FBF","E5A9FF",
                 "FFD6F6","FBEDFA"]

    accentColor = random.choice(colorList)
    return (accentColor)

def baseRandomizer():
    colorList = ["FFFDEA","FFEFDC","D8D6CD","FFFFFF","D8D7D8",
                "BBBABF","9D9D9F","808080","4D484F","636268","555555",
                "4B4946","352C27","333333","1D2224","BEA55D","C18E1B",
                "D1B300","FFEC80","EDE8B0","FDE9AC","FFD297","F6BF6C",
                "E8AF49","D1B045","B27749","C3996F","CABBA2","827A64",
                "6D675B","564D48","766259","977B6C","774840","603E3D",
                "57372C","301E1A","5A4534","72573A","855B33","91532A",
                "8E5B3F","563012","7B3C1D","FFD6F6","FBEDFA",
                "FEA0A0","E8FCB4","97AF8B","7ECE73","9AEAEF","72C4C4",
                "8DBCB4","E2FFE6","B2E2BD","9AFFC7","61AB89","E1CDFE",
                "CCA4E0","9778BE","C15A39","C47149","FFB576","993BD1",
                "7930B5","4D2C89","3F2B66","2D237A","0D0A5B","212B5F",
                "013485","1C51E7","0B2D46","0A3D67","CE000D","AA0024",
                "850012","581014","2D0102","8C272D","C1272D","DF3236",
                "8A024A","4D0F28"]



    accentColor = random.choice(colorList)
    return (accentColor)

def eyeRandomizer():
    colorList = [ "F9D0AB", "9E7556", "613612", "FEDDDD", "D95050"
                , "6E1919", "FBFEE6", "B5DE69", "547000", "c8f9fb"
                , "6EA7E4", "0A446F", "CEFDE6", "44D2AC", "1D6752"
                , "FEFFFF", "E7F5FF", "484B4F", "f7ecff", "C392F7"
                , "473658", "FFFDFB", "ECBA86", "554C3B", "FFC6FB"
                , "FDB7F1", "66005F", "D3FEC9", "73D37F", "255F26"
                , "FFEABE", "FFA150", "563400"]
    eyeColor = random.choice(colorList)

    return eyeColor
    

def eyeName(eyeColor):
    eye = "00"

    match eyeColor:
        case "F9D0AB":
            eye = "EL"
        case "9E7556":
            eye = "EB"
        case "613612":
            eye = "ED"
        case "FEDDDD":
            eye = "PL"
        case "D95050":
            eye = "PB"
        case "6E1919":
            eye = "PD"
        case "FBFEE6":
            eye = "WL"
        case "B5DE69":
            eye = "WB"
        case "547000":
            eye = "WD"
        #D = water droplet
        case "c8f9fb":
            eye = "DL"
        case "6EA7E4":
            eye = "DB"
        case "0A446F":
            eye = "DD"
        # N = liGHTILNG
        case "CEFDE6":
            eye = "GL"
        case "44D2AC":
            eye = "GB"
        case "1D6752":
            eye = "GD"
        case "FEFFFF":
            eye = "IL"
        case "E7F5FF":
            eye = "IB"
        case "484B4F":
            eye = "ID"
        case "f7ecff":
            eye = "SL"
        case "C392F7":
            eye = "SB"
        case "473658":
            eye = "SD"
        case "FFFDFB":
            eye = "LL"
        case "ECBA86":
            eye = "LB"
        case "554C3B":
            eye = "LD"
        case "FFC6FB":
            eye = "AL"
        case "FDB7F1":
            eye = "AB"
        case "66005F":
            eye = "AD"
        case "D3FEC9":
            eye = "NL"
        case "73D37F":
            eye = "NB"
        case "255F26":
            eye = "ND"
        case "FFEABE":
            eye = "FL"
        case "FFA150":
            eye = "FB"
        case "563400":
            eye = "FD"

    return eye

def patternName(pattern):

    match(pattern):
        case"solid":
            pat = "SO"
        case "chestnut":
            pat = "CN"
        case "sabino":
            pat = "SA"
        case "overo":
            pat = "OV"
        case "dapple":
            pat = "DA"
        case "tovero":
            pat = "TO"
        case "tobiano":
            pat = "TB"
        case "blanket":
            pat = "BT"
        case "leopard":
            pat = "LE"
        case "bay":
            pat = "BY"
        case "dun":
            pat = "DN"
        case "snowflake":
            pat = "SF"
        case "snowcap":
            pat = "SC"
        case "frost":
            pat = "FR"
        case "faire":
            pat = "FA"
        case "marble":
            pat = "MA"

    return pat


def hairName(name):

    match(name):
       
        case "short":
            hair = "SH"
        case "curly":
            hair = "CU"
        case "buns":
            hair = "BU"
        case "fishtail":
            hair = "FI"
        case "braids":
            hair = "BR"
        case "long":
            hair = "LO"
        case "wild":
            hair = "WI"
        case "summer":
            hair = "SU"
        case "wind":
            hair = "WN"
        case "winter":
            hair = "WT"
        case "water":
            hair = "WA"
        case "rock":
            hair = "RO"
        case "spring":
            hair = "SP"
        case "fall":
            hair = "FA"
        case "cirrus":
            hair = "CI"

    return hair


def accessoryName(acc):
    accessory = "none"

    match(acc):

        case "armorApeliotes" :
            accessory = "ARA"
        case  "armorBlack" :
            accessory = "ARB"
        case  "armorBoreas" :
            accessory = "ARO"
        case "armorNotus" :
            accessory = "ARN"
        case "armorWhite" :
            accessory = "ARW"
        case  "armorZephyrus" :
            accessory = "ARZ"
        case  "batBlack" :
            accessory = "BAB"
        case  "batRed" :
            accessory = "BAR"
        case "beretApeliotes" :
            accessory = "BEA"
        case "beretBoreas" :
            accessory = "BEB"
        case  "beretNotus" :
            accessory = "BEN"
        case  "beretZephyrus" :
            accessory = "BEZ"
        case "blanketApeliotes" :
            accessory = "BLA"
        case "blanketBoreas" :
            accessory = "BLB"
        case  "blanketNotus" :
            accessory = "BLN"
        case  "blanketZephyrus" :
            accessory = "BLZ"
        case "bridleBlack" :
            accessory = "BRL"
        case "bridleBrown" :
            accessory = "BRO"
        case  "carouselEastern" :
            accessory = "CAE"
        case  "carouselNorthern" :
            accessory = "CAN"
        case "carouselSouthern" :
            accessory = "CAS"
        case "carouselWestern" :
            accessory = "CAW"
        case  "cowboyBlack" :
            accessory = "COB"
        case  "cowboyDark" :
            accessory = "COD"
        case  "cowboyLight" :
            accessory = "COL"
        case "dressBlack" :
            accessory = "DRB"
        case  "dressBlue" :
            accessory = "DRU"
        case  "dressPink" :
            accessory = "DRP"
        case  "dressRed" :
            accessory = "DRR"
        case "firstRibbon" :
            accessory = "FIR"
        case "floofBlack" :
            accessory = "FLB"
        case  "floofWhite" :
            accessory = "FLW"
        case  "flowerYellow" :
            accessory = "FLY"
        case "flowerPurple" :
            accessory = "FLP"
        case "hoovesFire" :
            accessory = "HOI"
        case  "hoovesFlower" :
            accessory = "HOF"
        case  "hoovesWind" :
            accessory = "HOW"
        case  "lance" :
            accessory = "LAG"
        case "merBlue" :
            accessory = "MEB"
        case "merGreen" :
            accessory = "MEG"
        case  "merPurple" :
            accessory = "MEP"
        case  "pixieBlue" :
            accessory = "PIB"
        case  "pixieGreen" :
            accessory = "PIG"
        case  "pixiePink" :
            accessory = "PIP"
        case "pixiePurple" :
            accessory = "PIU"
        case  "ribbonPink" :
            accessory = "RIP"
        case  "ribbonPurple" :
            accessory = "RIU"
        case  "ribbonRed" :
            accessory = "RIR"
        case "saddleBlack" :
            accessory = "SAB"
        case  "saddleDark" :
            accessory = "SAD"
        case  "saddleLight" :
            accessory = "SAL"
        case  "shawlApeliotes" :
            accessory = "SHA"
        case "shawlBoreas" :
            accessory = "SHB"
        case "shawlNotus" :
            accessory = "SHN"
        case "shawlZephyrus" :
            accessory = "SHZ"            
        case  "wingAngel" :
            accessory = "WIA"
        case  "wingRaven" :
            accessory = "WIR"
        case  "none" :
            accessory = "NON"
        case  "shadowWitch" :
            accessory = "WHS"
        case  "fireWitch" :
            accessory = "WHF"
        case  "pinkWitch" :
            accessory = "WHP"
        case  "whiteWitch" :
            accessory = "WHW"
        case  "galaxyWitch" :
            accessory = "WHG"
        case  "darkLantern" :
            accessory = "LAD"
        case  "lightLantern" :
            accessory = "LAL"
        case "lagoonSilk" :
            accessory = "SIL"
        case "bloodsongSilk" :
            accessory = "SIB"
        case "nebulaSilk" :
            accessory = "SIN"
        case "verdantSilk" :
            accessory = "SIV"
        case "redRose" :
            accessory = "ROR"
        case "blueRose" :
            accessory = "ROB"
        case "pinkRose" :
            accessory = "ROP"
        case "cirrusGreenWings" :
            accessory = "CWG"
        case "cirrusWhiteWings" :
            accessory = "CWW"
        case "blackClaws" :
            accessory = "CLB" 
        case  "redClaws" :        
            accessory = "CLR"


    return accessory

def patternSelector():

    chance = random.randint(1,100)

    if chance <= 100:
        patternList = ["solid", "chestnut", "sabino", "overo", "dapple",
                       "tovero", "tobiano", "blanket", "leopard", "bay", 
                       "dun", "snowflake", "snowcap", "frost", "faire", 
                       "marble"]
    pattern = random.choice(patternList)
    #print(pattern, end=" ")
    
    return pattern

def hairSelector():

    chance = random.randint(1,100)

    if chance <= 100:
        patternList = ["short", "curly", "buns", "fishtail", "braids",
                       "long", "wild", "summer", "wind", "winter", 
                       "water", "rock", "spring", "fall","cirrus"]
    pattern = random.choice(patternList)
    
    return pattern


def accessorySelector():

    chance = random.randint(1,100)

    if chance <= 70:
        patternList = ["armorApeliotes", "armorBlack", "armorBoreas", "armorNotus",
                       "armorWhite", "armorZephyrus", "batBlack", "batRed", "beretApeliotes",
                       "beretBoreas", "beretNotus", "beretZephyrus", "blanketApeliotes",
                       "blanketBoreas", "blanketNotus", "blanketZephyrus", "bridleBlack",
                       "bridleBrown", "carouselEastern", "carouselNorthern", "carouselSouthern",
                       "carouselWestern", "cowboyBlack", "cowboyDark", "cowboyLight", 
                       "dressBlack", "dressBlue", "dressPink", "dressRed", "firstRibbon",
                       "floofBlack", "floofWhite", "flowerYellow", "flowerPurple",
                       "hoovesFire", "hoovesFlower", "hoovesWind", "lance", "merBlue",
                       "merGreen", "merPurple", "pixieBlue", "pixieGreen", "pixiePink", 
                       "pixiePurple", "ribbonPink", "ribbonPurple", "ribbonRed", "saddleBlack",
                       "saddleDark", "saddleLight", "shawlApeliotes", "shawlBoreas",
                       'shawlNotus', "shawlZephyrus", "wingAngel", "wingRaven", "none"]
    else:
        patternList = ["shadowWitch","fireWitch","pinkWitch","whiteWitch","galaxyWitch",
                       "darkLantern","lightLantern",
                       "lagoonSilk","bloodsongSilk","nebulaSilk","verdantSilk",
                       "redRose","blueRose","pinkRose",
                       "cirrusGreenWings","cirrusWhiteWings",
                       "blackClaws","redClaws"]    
    pattern = random.choice(patternList)


    
    return pattern


# This method changes the hexcodes to the rgb values required for the color replacer 
# to function correctly. Do not change this section.
def hex_rgba(hex):
    rgb = []
    for i in (0, 2, 4):
      decimal = int(hex[i:i+2], 16)
      rgb.append(decimal)
    
    return tuple(rgb)



# DO NOT change this section. This is what actually goes through and replaces your pixels.
# Remember that it searches for white (#FFFFFF) pixels to replace, and that all pixels
# will be replaced at full opacity.
def pixelReplacer(partImage, color, datas):

    pixelColor = hex_rgba(color)

    red, green, blue, alpha = datas.T # Temporarily unpack the bands for readability

    white_areas = (red == 255) & (blue == 255) & (green == 255)
    datas[..., :-1][white_areas.T] = pixelColor # Transpose back needed

    partImage = Image.fromarray(datas)

    return partImage


##########################
##########################
##########################

def main():

    for i in range(50):

        x = 801 + i

        filename = str(x)

        # Pattern Type Select
        pattern = patternSelector()

        # Hair Type Select
        hair = hairSelector()

        # Accessory Type Select
        accessory = accessorySelector()   
        ####
        #accessory = "shawlZephyrus"  

        # Body Change
        baseImage = Image.open("images\\baseColor.png")
        baseImage = baseImage.convert("RGBA")
        datas = np.array(baseImage)
        baseColor = baseRandomizer()
        baseDatas = np.array(baseImage)        
        baseImage = pixelReplacer(baseImage, baseColor, baseDatas)       


        # Hair Change
        hairImage = Image.open("images\\" + hair + "Color.png")
        hairImage = hairImage.convert("RGBA")
        hairDatas = np.array(hairImage)
        hairColor = hairRandomizer()
        hairImage = pixelReplacer(hairImage, hairColor, hairDatas)

#        # Base Change
#        baseImage = Image.open("images\\baseColor.png")
#        baseImage = baseImage.convert("RGBA")
#        datas = baseImage.getdata()


#       randBaseColor = baseRandomizer()
#        randBaseColor = baseRandomizer()
        #base is: 
#        baseColor = hex_rgba(randBaseColor)

#        baseImage = pixelReplacer(baseImage,baseColor,datas)
    

        # Hair Change
#        hairImage = Image.open("images\\" + hair + "Color.png")
#        hairImage = hairImage.convert("RGBA")
#        datas = hairImage.getdata()

#        randhairColor = hairRandomizer()

        # hair is:

 #       hairColor = hex_rgba(randhairColor)

#        hairImage = pixelReplacer(hairImage,hairColor,datas)


        # Eyes Change
#        eyesImage = Image.open("images\\eyes.png")
#        eyesImage = eyesImage.convert("RGBA")
#        datas = eyesImage.getdata()

#        randEyeColor = eyeRandomizer()

#        eyesColor = hex_rgba(randEyeColor)

#        eyesImage = pixelReplacer(eyesImage,eyesColor,datas)

        # Eyes Change
        eyesImage = Image.open("images\\eyes.png")
        eyesImage = eyesImage.convert("RGBA")
        eyesDatas = np.array(eyesImage)
        eyesColor = eyeRandomizer()
        eyesImage = pixelReplacer(eyesImage, eyesColor, eyesDatas)


        filename += "-" + patternName(pattern)
        filename += "-" + baseColor        
        filename += "-" + eyeName(eyesColor)
        filename += "-" + hairName(hair)
        filename += "-" + hairColor
        filename += "-" + accessoryName(accessory)


        # Some parts (like shadows, lighting, lineart, etc) won't need to be recolored
        # or otherwise changed by the program. The program needs to open them to be able
        # to combine them into one image later, so open all other necessary images here.

        # Shadow (and Extras)
        shadowImage = Image.open("images\\baseShadow.png")

        shadowHairImage = Image.open("images\\" + hair + "Shadow.png")

        # Linework
        lineworkImage = Image.open("images\\base.png")

        # Hair Linework
        hairlineImage = Image.open("images\\" + hair + ".png")

        # Pattern
        patternImage = Image.open("images\\" + pattern + ".png")

        # Accessory
        accessoryImage = Image.open("images\\accessories\\" + accessory + ".png")

        #Composite
        background = baseImage
        foreground = patternImage

        generatedImage = Image.alpha_composite(background, foreground)

        ####################
        ##### Base Shadow #####

        # Import background image
        generatedImage_reg = np.array(generatedImage)  # Inputs to blend_modes need to be np arrays.
        generatedImage_float = generatedImage_reg.astype(float)  # Inputs to blend_modes need to be floats.        
        #generatedImage = np.array(generatedImage_raw)  # Inputs to blend_modes need to be np arrays.
        #generatedImage_float = generatedImage.astype(float)  # Inputs to blend_modes need to be floats.

        # Import foreground image
        shadowImage_reg = np.array(shadowImage)  # Inputs to blend_modes need to be np arrays.
        shadowImage_float = shadowImage_reg.astype(float)  # Inputs to blend_modes need to be floats.

        # Blend images
        generatedImage_float = multiply(generatedImage_float, shadowImage_float, 0.7)

        # Convert blended image back into PIL image
        generated_image = np.uint8(generatedImage_float)  # Image needs to be converted back to uint8 type for PIL handling.
        generatedImage = Image.fromarray(generated_image)


        #generatedImage = Image.alpha_composite(background, foreground)

        #background = generatedImage
        #foreground = shadowImage        

        #generatedImage = Image.alpha_composite(background, foreground)

        background = generatedImage
        foreground = eyesImage

        generatedImage = Image.alpha_composite(background, foreground)

        background = generatedImage
        foreground = lineworkImage

        generatedImage = Image.alpha_composite(background, foreground)

        background = generatedImage
        foreground = hairImage

        generatedImage = Image.alpha_composite(background, foreground)


        ####################
        ##### Hair Shadow #####

        # Import background image
        generatedImage_reg = np.array(generatedImage)  # Inputs to blend_modes need to be np arrays.
        generatedImage_float = generatedImage_reg.astype(float)  # Inputs to blend_modes need to be floats.        
        #generatedImage = np.array(generatedImage_raw)  # Inputs to blend_modes need to be np arrays.
        #generatedImage_float = generatedImage.astype(float)  # Inputs to blend_modes need to be floats.

        # Import foreground image
        shadowImage_reg = np.array(shadowHairImage)  # Inputs to blend_modes need to be np arrays.
        shadowImage_float = shadowImage_reg.astype(float)  # Inputs to blend_modes need to be floats.

        # Blend images
        generatedImage_float = multiply(generatedImage_float, shadowImage_float, 0.7)

        # Convert blended image back into PIL image
        generated_image = np.uint8(generatedImage_float)  # Image needs to be converted back to uint8 type for PIL handling.
        generatedImage = Image.fromarray(generated_image)


        background = generatedImage
        foreground = hairlineImage

        generatedImage = Image.alpha_composite(background, foreground)


        background = generatedImage
        foreground = accessoryImage

        generatedImage = Image.alpha_composite(background, foreground)


        generatedImage.save(filename + ".png", "PNG")

        print(filename)

    print("-------------------------")

    


if __name__ == "__main__":
    main()
