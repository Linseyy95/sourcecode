thinLineWidth = 0.1
thickLineWidth = 1.2

def drawBackground():
    y = 1
    for i in range(44):
        shadow(None)
        strokeWidth(thinLineWidth * gridSizeY)
        stroke(0.9)
        line((0*gridSizeX, y*gridSizeY), (73*gridSizeX, y*gridSizeY))
        y = y + 1

def drawShape(shape):
    y = 1
    extent = 0
    for lines in shape:
        shadow(None)
        strokeWidth(thinLineWidth * gridSizeY)
        stroke(0.9)
        
        shadow((0.9, -0.9), 6.0, (0, 0, 0))
        strokeWidth(thickLineWidth * gridSizeY)
        for a, b in lines:
            line((a*gridSizeY, y*gridSizeX), (b*gridSizeY, y*gridSizeX))
            extent = max(extent, b)
        y = y + 1
    return extent


letter_A = [
            [],
            [(1,4), (9,13)],
            [(1.5, 3), (10,12.5)],
            [(2,3), (10,12)],
            [(2,3), (10,12)],
            [(2,3), (10,12)],
            [(2,12)],
            [(2,3), (10,12)],
            [(2,3), (10,12)],
            [(2,3), (10,12)],
            [(2.5,3.5), (9,11.5)],
            [(3,4), (8.5,11)],
            [(4,10.5)], 
            []
            ]
            
letter_E = [
            [],
            [(1,12)],
            [(1.5,4), (10,12)],
            [(2,4), (11,12)],
            [(2,4)],
            [(2,4), (7,8)],
            [(2,8)],
            [(2,4), (7,8)],
            [(2,4)],
            [(2,4)],
            [(2,4), (11,12)],
            [(1.5,4), (10,12)],
            [(1,12)], 
            []
            ]
            
letter_F = [
            [],
            [(1,5)],
            [(1.5,4)],
            [(2,4)],
            [(2,4)],
            [(2,4), (7,8)],
            [(2,8)],
            [(2,4), (7,8)],
            [(2,4)],
            [(2,4)],
            [(2,4), (11,12)],
            [(1.5,4), (10,12)],
            [(1,12)], 
            []
            ]
            
letter_N = [
            [],
            [(1,4), (8.2, 12)],
            [(1.5,3), (7.8, 12)],
            [(2,3), (7.4, 9.4), (11,12)],
            [(2,3), (7, 9), (11,12)],
            [(2,3), (6.6, 8.6), (11,12)],
            [(2,3), (6.2, 8.2), (11,12)],
            [(2,3), (5.8, 7.8), (11,12)],
            [(2,3), (5.4, 7.4), (11,12)],
            [(2,3), (5, 7), (11,12)],
            [(2,3), (4.6, 6.6), (11,12)],
            [(2,6.5), (10.5,12.5)],
            [(1,6), (10,13)], 
            []
            ]

letter_P = [
            [], 
            [(1,5)],
            [(1.5,4)],
            [(2,4)],
            [(2,4)],
            [(2,4)],
            [(2,10)],
            [(2,4), (9,11)],
            [(2,4), (10,12)],
            [(2,4), (10,12)],
            [(2,4), (10,12)],
            [(1.5,4), (9,11)],
            [(1,10)], 
            []
            ]
            
letter_R = [
            [], 
            [(1,5), (9,12)],
            [(1.5,4), (9,11)],
            [(2,4), (8.5,10.5)],
            [(2,4), (7.5,9.5)],
            [(2,4), (6.5,8.5)],
            [(2,10)],
            [(2,4), (9,11)],
            [(2,4), (10,12)],
            [(2,4), (10,12)],
            [(2,4), (10,12)],
            [(1.5,4), (9,11)],
            [(1,10)], 
            []
            ]
                    
letter_S = [
            [], 
            [(3,10)],
            [(1.5,4), (8.5,11)],
            [(1,3), (9.5,12)],
            [(1,2), (7.5, 11.5)],
            [ (6.2, 10.2)],
            [(5.0, 9.0)],
            [(3.7, 7.7)],
            [(2.5, 6.5)],
            [(1.5, 4.5)],
            [(1,3), (10,12)],
            [(1.5,4), (8.5,11)],
            [(2.5,10.5)], 
            []
            ]
            
letter_T = [
            [], 
            [(4,9)],
            [(5,8)],
            [(5.5,7.5)],
            [(5.5,7.5)],
            [(5.5,7.5)],
            [(5.5,7.5)],
            [(5.5,7.5)],
            [(5.5,7.5)],
            [(5.5,7.5)],
            [(1,2), (5.5,7.5), (11,12)],
            [(1,3), (5.5,7.5), (10,12)],
            [(1,12)],
            []
            ]
            
letter_U = [
            [], 
            [(4,10)],
            [(3,6), (10,11)],
            [(2,5), (10.5,11.5)],
            [(2,4), (11,12)],
            [(2,4), (11,12)],
            [(2,4), (11,12)],
            [(2,4), (11,12)],            
            [(2,4), (11,12)],
            [(2,4), (11,12)],
            [(2,4), (11,12)],
            [(1.5, 4), (10.5,12)],
            [(1,5), (10,12)],
            []
            ]
            
            
fontDictionary = {
    "A": letter_A,
    "E": letter_E,
    "F": letter_F,
    "N": letter_N,
    "P": letter_P,
    "R": letter_R,
    "S": letter_S,
    "T": letter_T,
    "U": letter_U,
    }
    
def drawLetters(txt):
    save()
    for char in txt:
        if char in fontDictionary:
            shape = fontDictionary[char]
            extent = drawShape(shape)
            translate((extent + 1) * gridSizeX, 0)
    restore()

numFrames = 20

for frame in range(numFrames):
    t = frame / numFrames

    newPage(1500, 912)

    fill(0)
    rect(0, 0, width(), height())
    scale(1)

    gridSizeX = 20
    gridSizeY = 20

    fill(None)
    stroke(0)
    lineCap("round")

    thickLineWidth = 0.05
    translate(20, 0)
    drawBackground()
    
    
    translate(50, 460)
    
    thickLineWidth = 0 + (sin(2 * pi * t - 0.5*pi) + 1) / 2
    drawLetters("EAT")
    
    translate(0, -16 * gridSizeX)
    
    thickLineWidth = 0 + (sin(2 * pi * t - 0.5*pi) + 1) / 2
    drawLetters("PASTA")

for frame in range(numFrames):
    t = frame / numFrames

    newPage(1500, 912)

    fill(0)
    rect(0, 0, width(), height())
    scale(1)

    gridSizeX = 20
    gridSizeY = 20

    fill(None)
    stroke(0)
    lineCap("round")

    thickLineWidth = 0.05
    translate(20, 0)
    drawBackground()
    
    
    translate(50, 460)
        
    thickLineWidth = 0 + (sin(2 * pi * t - 0.5*pi) + 1) / 2
    drawLetters("RUN")
    
    translate(0, -16 * gridSizeX)
    
    thickLineWidth = 0 + (sin(2 * pi * t - 0.5*pi) + 1) / 2
    drawLetters("FASTA")


    
    
    saveImage("EATPASTA2.gif")
