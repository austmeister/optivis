# Optivis #

![example](https://cloud.githubusercontent.com/assets/5225190/5718217/570c509a-9b03-11e4-8e4a-65114fb75d43.png)

Script to visualise optical environments. Uses the fantastic SVG optical components created by Alexander Franzen (http://www.gwoptics.org/ComponentLibrary/).  

## Requirements ##
Optivis requires the following components:

* Python 2.7+
* python-qt4

On Ubuntu/Debian you should be able to install these with the following command:

`~$ sudo apt-get install python python-qt4`

## Coordinate System ##
Optivis uses a left-handed coordinate system in line with almost all computer graphics applications. Positive angle rotations are clockwise. All geometrical transforms are performed with the coordinate class contained in `optivis.geometry`.

## Adding New Components ##
Optivis uses scalable vector graphics (SVGs) as a basis for its optical components. To add a new component, you must provide an SVG file describing the component's looks. Please use one of the existing files as a basis for your design - Optivis expects SVG files to have a specific format:
 * The root element should be an `<svg>` item (this is standard for the SVG file format anyway).
 * Elements and element attributes should not use namespaces (such as `i:midPoint="value"`), because namespaces are not defined in the header. This is to keep the files clean of program-specific crud, and ensure that generated SVG files are [valid](http://validator.w3.org/).
 * The use of ID attributes should be restricted to definitions of IDs in elements (such as `<g id="this-id">`) and URLs (such as `fill="url(#gradient-id)"`). This is because Optivis replaces IDs in SVG files with unique strings, to allow multiple versions of the same component to be grouped together in a generated scene. The use of IDs in any other form may result in display issues.

The SVG file should be given an appropriate filename and placed in the `assets` directory within the `optivis` package. Then, in `optivis.bench.components` you should subclass the `AbstractComponent` class and write a constructor - see the existing components for details of how to do this. You will have to define nodes for your component's inputs and outputs. Nodes are places where links can originate or terminate, and must be positioned on the component's normalised coordinate system, where the origin is in the centre of the component. Again, see existing components for details.

## Planned Features ##
At some undetermined time in the future, I hope to have added the following features:
 * More components from Alexander Franzen's graphics set
 * Link colours validated properly (right now you speicify a Qt colour class, but it would be nice to specify e.g. 'red' instead)
 * Export to SVG pays attention to link colours
 * PDF export
 * Electronics (e.g. local oscillator), with sensible routing
 * Patterned links, e.g. dashed links to represent squeezed light
 * GUI edit features:
   - Add/delete/edit component
   - Change layout manager (need other layout managers first...)
   - Add tooltips/notes
 * Load existing SVG and interpret the components in it (might require version number to be embedded in files to change load behaviour for older files) - hopefully loading a file and saving it without changes will produce an exact copy

Sean Leavey  
https://github.com/SeanDS/
