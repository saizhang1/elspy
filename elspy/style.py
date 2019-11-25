""" Elsevier branding styles.

See http://design.elsevier.com/styleguide/
"""


class Font():
	name = 'Arial'


class RGB():
	orange = [255, 130, 0]
	blue = [0, 115, 152]
	white = [255, 255, 255]
	grey_light = [245, 245, 245]
	grey_light2 = [235, 235, 235]
	grey = [150, 150, 150]
	grey_dark = [80, 80, 80]
	colorbar = [
		[255, 130, 0], #FF8200 # elsevier orange
		[0, 115, 152], #007398 # elsevier blue
	    [193, 194, 195], #C1C2C3 # elsevier light grey
	    [65, 182, 230], #41B6E6 # elsevier light blue
	    [117, 120, 123], #75787B # elsevier dark grey
	    [255, 180, 102], #FFB466 # elsevier2 light orange
	    #[102, 171, 193], #66ABC1 # elsevier2 light blue1
	    [206, 220, 0], #CEDC00 # elsevier2 yellow-green
	    [0, 129, 10], #00816D # elsevier2 blue-green
	    #[100, 204, 201], #64CCC9 # elsevier2 light blue2
		[255, 255, 0], #FFFF00 microsoft yellow
		[146, 208, 80], #92D050 # microsoft light green
		[255, 192, 0], #FFC000 # microsoft orange
		[112, 48, 160], #7030A0 # microsoft purple
		#[0, 176, 80], #00B050 # microsoft green
		[0, 32, 96], #002060 # microsoft dark blue
		#[0, 112, 192], #0070C0 # microsoft blue
		[192, 0, 0] #C00000 # microsoft dark red
		#[0, 176, 240], #00B0F0 # microsoft light blue
		#[255, 0, 0], #FF0000 # microsoft red
	]


class Hex():
	orange = '#ff8200'
	blue = '#007398'
	white = '#FFFFFF'
	grey_light = '#F5F5F5'
	grey_light2 = '#EBEBEB'
	grey = '#969696'
	grey_dark = '#505050'
	colorbar = [
	    '#FF8200', # elsevier orange #[255, 130, 0]
	    '#007398', # elsevier blue #[0, 115, 152]
	    '#C1C2C3', # elsevier light grey #[193, 194, 195]
	    '#41B6E6', # elsevier light blue #[65, 182, 230]
	    '#75787B', # elsevier dark grey #[117, 120, 123]
	    '#FFB466', # elsevier2 light orange #[255, 180, 102]
	    #'#66ABC1', # elsevier2 light blue1 #[102, 171, 193]
	    '#CEDC00', # elsevier2 yellow-green #[206, 220, 0]
	    '#00816D', # elsevier2 blue-green #[0, 129, 10]
	    #'#64CCC9', # elsevier2 light blue2 #[100, 204, 201]
		'#FFFF00', # microsoft yellow
		'#92D050', # microsoft light green
		'#FFC000', # microsoft orange
		'#7030A0', # microsoft purple
		#'#00B050', # microsoft green
		'#002060', # microsoft dark blue
		#'#0070C0', # microsoft blue
		'#C00000' # microsoft dark red
		#'#00B0F0', # microsoft light blue
		#'#FF0000', # microsoft red
	]

class MPL():
	figure_settings = {
	    'titlesize': 32,
	    'figsize': (16,10), #offset +1 for bottom legend, located at 20% below x-axis
		'dpi': 700
	}
	font_settings = {
	    'family': 'sans-serif',
	    'serif': 'Arial',
	    'size': 16,
	}
	text_settings = {
		'color': Hex.grey_dark
	}
	axes_settings = {
	    'titlesize': 24,
	    'labelsize': 18,
		'labelcolor': Hex.grey_dark,
		'spines.left': True,
		'spines.bottom': True,
		'spines.top': False,
		'spines.right': False
	}
	xtick_settings = {
	    'rotation': 'horizontal',
	    'labelsize': 14,
		'color': Hex.grey,
		'direction': 'out',
		'major.size': 6,
		'major.width': 2,
		'minor.visible': False
	}
	ytick_settings = {
	    'labelsize': 14,
		'color': Hex.grey,
		'direction': 'out',
		'major.size': 6,
		'major.width': 2,
		'minor.visible': False
	}
	legend_settings = {
	    'loc': 'upper center',
		'bbox_to_anchor': [0.5,-0.1],
		'frameon': False,
	    'fontsize': 12,
		'framealpha': 0
	}
	line_settings = {
	    'linewidth': 4
	}
	hatch_settings = {
		'color': Hex.grey_dark
	}
	savefig_settings = {
	    'transparent': True,
	    'dpi': 300,
	    'bbox': 'tight',
	    'pad_inches': .05,
	    'format': 'png' #python-docx has limited support for image files
	}
