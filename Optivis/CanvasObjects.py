from __future__ import division
import Tkinter as Tk
import BenchObjects

class CanvasObject(object):
  def __init__(self):
    return None

  # FIXME: make draw() an abstract class

class CanvasComponent(CanvasObject):
  def __init__(self, component, azimuth=0, xPos=0, yPos=0):
    if not isinstance(component, BenchObjects.Component):
      raise Exception('Specified component is not of type BenchObjects.Component')
    
    self.azimuth = azimuth
    self.image = None

    self.component = component
    self.xPos = xPos
    self.yPos = yPos

    super(CanvasComponent, self).__init__()
  
  def draw(self, canvas, svgDir):
    if not isinstance(canvas, Tk.Canvas):
      raise Exception('Specified canvas is not of type Tk.Canvas')

    canvas.create_image(self.xPos, self.yPos, image=self.getImage(svgDir=svgDir), anchor=Tk.CENTER)

  @property
  def xPos(self):
    return self.__xPos
  
  @xPos.setter
  def xPos(self, xPos):
    self.__xPos = xPos
  
  @property
  def yPos(self):
    return self.__yPos
  
  @yPos.setter
  def yPos(self, yPos):
    self.__yPos = yPos
  
  def getImage(self, svgDir):
    self.image = self.component.toImage(svgDir=svgDir, azimuth=self.azimuth)
    
    return self.image
  
  @property
  def azimuth(self):
    return self.__azimuth
  
  @azimuth.setter
  def azimuth(self, azimuth):
    self.__azimuth = azimuth
    
  def __str__(self):
    # return component's __str__
    return self.component.__str__()

class CanvasLink(CanvasObject):
  def __init__(self, (xStart, yStart), (xEnd, yEnd), fill="red", startMarker=True, endMarker=True, startMarkerRadius=3, endMarkerRadius=2, startMarkerOutline="red", endMarkerOutline="blue"):
    self.startPos = (xStart, yStart)
    self.endPos = (xEnd, yEnd)
    self.fill = fill
    self.startMarker = startMarker
    self.endMarker = endMarker
    self.startMarkerRadius = startMarkerRadius
    self.endMarkerRadius = endMarkerRadius
    self.startMarkerOutline = startMarkerOutline
    self.endMarkerOutline = endMarkerOutline
    
    super(CanvasLink, self).__init__()

  def draw(self, canvas, svgDir):
    if not isinstance(canvas, Tk.Canvas):
      raise Exception('Specified canvas is not of type Tk.Canvas')

    canvas.create_line(self.startPos[0], self.startPos[1], self.endPos[0], self.endPos[1], fill=self.fill)
    
    # add markers if necessary
    if self.startMarker: canvas.create_oval(self.startPos[0] - self.startMarkerRadius, self.startPos[1] - self.startMarkerRadius, self.startPos[0] + self.startMarkerRadius, self.startPos[1] + self.startMarkerRadius, outline=self.startMarkerOutline, tags="startmarker")
    if self.endMarker: canvas.create_oval(self.endPos[0] - self.endMarkerRadius, self.endPos[1] - self.endMarkerRadius, self.endPos[0] + self.endMarkerRadius, self.endPos[1] + self.endMarkerRadius, outline=self.endMarkerOutline, tags="endmarker")

  @property
  def startPos(self):
    return self.__startPos

  @startPos.setter
  def startPos(self, startPos):
    self.__startPos = startPos

  @property
  def endPos(self):
    return self.__endPos

  @endPos.setter
  def endPos(self, endPos):
    self.__endPos = endPos

  @property
  def fill(self):
    return self.__fill

  @fill.setter
  def fill(self, fill):
    self.__fill = fill
    
  @property
  def startMarker(self):
    return self.__startMarker
  
  @startMarker.setter
  def startMarker(self, startMarker):
    self.__startMarker = startMarker
    
  @property
  def endMarker(self):
    return self.__endMarker
  
  @endMarker.setter
  def endMarker(self, endMarker):
    self.__endMarker = endMarker
    
  @property
  def startMarkerRadius(self):
    return self.__startMarkerRadius
  
  @startMarkerRadius.setter
  def startMarkerRadius(self, startMarkerRadius):
    self.__startMarkerRadius = startMarkerRadius
    
  @property
  def endMarkerRadius(self):
    return self.__endMarkerRadius
  
  @endMarkerRadius.setter
  def endMarkerRadius(self, endMarkerRadius):
    self.__endMarkerRadius = endMarkerRadius
    
  @property
  def startMarkerOutline(self):
    return self.__startMarkerOutline
  
  @startMarkerOutline.setter
  def startMarkerOutline(self, startMarkerOutline):
    self.__startMarkerOutline = startMarkerOutline
    
  @property
  def endMarkerOutline(self):
    return self.__endMarkerOutline
  
  @endMarkerOutline.setter
  def endMarkerOutline(self, endMarkerOutline):
    self.__endMarkerOutline = endMarkerOutline