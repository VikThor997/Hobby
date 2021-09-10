from vpython import * # import kniznice VisualPython // kompletna kniznica
from time import * # import kniznice time // funkcie ako delay 
BallRadius = .75 # parametrizovanie gule
wallThickness = .1 # parametrizovanie miestnosti
wallWidth = 15 # ----//-------------------------
wallDepth = 12 # ----//-------------------------
wallHeight = 10 # ---//-------------------------
Floor = box(pos = vector(0,-wallHeight/2,0), color = color.red, size = vector(wallWidth, wallThickness,wallDepth)) # tvorba podlahy + definicia polohy
Ceiling = box(pos = vector(0,wallHeight/2,0), color = color.red, size = vector(wallWidth, wallThickness,wallDepth)) # tvorba stropu -//---------------
LeftWall = box(pos = vector(wallWidth/2,0,0), color = color.red, size = vector(wallThickness,wallHeight,wallDepth)) # lava stena 
RightWall = box(pos = vector(-wallWidth/2,0,0), color = color.red, size = vector(wallThickness,wallHeight,wallDepth)) # prava stena
BackWall = box(pos = vector(0,0,-wallDepth/2), color = color.red, size = vector(wallWidth,wallHeight,wallThickness)) # zadna stena
Ball = sphere(color = color.white, radius = BallRadius) # tvorba gulicky
deltaX = .1 # inkrement X-os
deltaY = .1 # -//------ Y-os
deltaZ = .1 # -//------ Z-os
xPos = 0 # deklaracia pociatocnej polohy X suradnica
yPos = 0 # ----//----------------------- Y suradnica
zPos = 0 # ----//----------------------- Z suradnica

while True: # nekonecny cyklus
    rate(50) # rychlost prehravania, vyssi rate = vyssia rychlost prehrania
    xPos = xPos + deltaX # inkrementalny pridavok k pozicii X-ovy smer
    yPos = yPos + deltaY # ----//-------------------------- Y-ovy smer
    zPos = zPos + deltaZ # ----//-------------------------- Z-ovy smer
    xRightBallEdge = xPos + BallRadius # hranicny bod gulocky // pravy extrem // sluzi na presny odraz od steny
    xLeftBallEdge = xPos - BallRadius # --//----------------- // lavy extrem // -----//-------------------------
    yTopBallEdge = yPos + BallRadius # ---//----------------- // horny extrem // ----//-------------------------
    yBotBallEdge  = yPos - BallRadius # --//----------------- // dolny extrem // ----//-------------------------
    zFrontBallEdge = zPos + BallRadius # -//----------------- // predny extrem // ---//-------------------------
    zBackBallEdge = zPos - BallRadius # --//----------------- // zadny extrem // ----//-------------------------

    RightWallEdge = wallWidth/2 - wallThickness/2 # definicia hranicnych bodov steny 
    LelfWallEdge = -wallWidth/2 + wallThickness/2 # ----//--------------------------
    TopWallEdge = wallHeight/2 - wallThickness/2 # ---- //--------------------------
    BottomWallEdge = -wallHeight/2 + wallThickness/2 # -//--------------------------
    FrontWallEdge = wallDepth/2 - wallThickness/2 # ----//--------------------------
    BackWallEdge = -wallDepth/2 + wallThickness/2 # ----//--------------------------

    if (xRightBallEdge >= RightWallEdge or xLeftBallEdge <= LelfWallEdge): # podmienka pre odraz // X-ovy smer
        deltaX = deltaX*(-1) # zmena znamienka na inkremente -> opacny smer 
    if (yTopBallEdge >= TopWallEdge  or yBotBallEdge <= BottomWallEdge): # Y-ovy smer
        deltaY = deltaY*(-1)
    if (zFrontBallEdge >= FrontWallEdge or zBackBallEdge <= BackWallEdge): # Z-ovy smer
        deltaZ = deltaZ*(-1)
    Ball.pos = vector(xPos,yPos,zPos) # parametrizovana poloha gulocky