#stretch: included extensive known formulas dictionary, included function to print name of formula if known, and if unknown, ask user for name to add to dictionary.
from formula import parse_formula

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

periodic_table_list = [
["Ac",	"Actinium",	227],
["Ag",	"Silver",	107.8682],
["Al",	"Aluminum",	26.9815386],
["Ar",	"Argon",	39.948],
["As",	"Arsenic",	74.9216],
["At",	"Astatine",	210],
["Au",	"Gold",	196.966569],
["B",	"Boron",	10.811],
["Ba",	"Barium",	137.327],
["Be",	"Beryllium",	9.012182],
["Bi",	"Bismuth",	208.9804],
["Br",	"Bromine",	79.904],
["C",	"Carbon",	12.0107],
["Ca",	"Calcium",	40.078],
["Cd",	"Cadmium",	112.411],
["Ce",	"Cerium",	140.116],
["Cl",	"Chlorine",	35.453],
["Co",	"Cobalt",	58.933195],
["Cr",	"Chromium",	51.9961],
["Cs",	"Cesium",	132.9054519],
["Cu",	"Copper",	63.546],
["Dy",	"Dysprosium",	162.5],
["Er",	"Erbium",	167.259],
["Eu",	"Europium",	151.964],
["F",	"Fluorine",	18.9984032],
["Fe",	"Iron",	55.845],
["Fr",	"Francium",	223],
["Ga",	"Gallium",	69.723],
["Gd",	"Gadolinium",	157.25],
["Ge",	"Germanium",	72.64],
["H",	"Hydrogen",	1.00794],
["He",	"Helium",	4.002602],
["Hf",	"Hafnium",	178.49],
["Hg",	"Mercury",	200.59],
["Ho",	"Holmium",	164.93032],
["I",	"Iodine",	126.90447],
["In",	"Indium",	114.818],
["Ir",	"Iridium",	192.217],
["K",	"Potassium",	39.0983],
["Kr",	"Krypton",	83.798],
["La",	"Lanthanum",	138.90547],
["Li",	"Lithium",	6.941],
["Lu",	"Lutetium",	174.9668],
["Mg",	"Magnesium",	24.305],
["Mn",	"Manganese",	54.938045],
["Mo",	"Molybdenum",	95.96],
["N",	"Nitrogen",	14.0067],
["Na",	"Sodium",	22.98976928],
["Nb",	"Niobium",	92.90638],
["Nd",	"Neodymium",	144.242],
["Ne",	"Neon",	20.1797],
["Ni",	"Nickel",	58.6934],
["Np",	"Neptunium",	237],
["O",	"Oxygen",	15.9994],
["Os",	"Osmium",	190.23],
["P",	"Phosphorus",	30.973762],
["Pa",	"Protactinium",	231.03588],
["Pb",	"Lead",	207.2],
["Pd",	"Palladium",	106.42],
["Pm",	"Promethium",	145],
["Po",	"Polonium",	209],
["Pr",	"Praseodymium",	140.90765],
["Pt",	"Platinum",	195.084],
["Pu",	"Plutonium",	244],
["Ra",	"Radium",	226],
["Rb",	"Rubidium",	85.4678],
["Re",	"Rhenium",	186.207],
["Rh",	"Rhodium",	102.9055],
["Rn",	"Radon",	222],
["Ru",	"Ruthenium",	101.07],
["S",	"Sulfur",	32.065],
["Sb",	"Antimony",	121.76],
["Sc",	"Scandium",	44.955912],
["Se",	"Selenium",	78.96],
["Si",	"Silicon",	28.0855],
["Sm",	"Samarium",	150.36],
["Sn",	"Tin",	118.71],
["Sr",	"Strontium",	87.62],
["Ta",	"Tantalum",	180.94788],
["Tb",	"Terbium",	158.92535],
["Tc",	"Technetium",	98],
["Te",	"Tellurium",	127.6],
["Th",	"Thorium",	232.03806],
["Ti",	"Titanium",	47.867],
["Tl",	"Thallium",	204.3833],
["Tm",	"Thulium",	168.93421],
["U",	"Uranium",	238.02891],
["V",	"Vanadium",	50.9415],
["W",	"Tungsten",	183.84],
["Xe",	"Xenon",	131.293],
["Y",	"Yttrium",	88.90585],
["Yb",	"Ytterbium",	173.054],
["Zn",	"Zinc",	65.38],
["Zr",	"Zirconium",	91.224]
]

known_molecules_dict = {
    "H2O": "water",
    "H2O2": "hydrogen peroxide",
    "NH3": "ammonia",
    "CH4": "methane",
    "C2H5OH": "ethanol",
    "C6H12O6": "glucose",
    "CO2": "carbon dioxide",
    "O2": "oxygen",
    "N2": "nitrogen",
    "NaCl": "sodium chloride",
    "C6H6": "benzene",
    "C7H8": "toluene",
    "C6H5OH": "phenol",
    "C6H5CH3": "toluene",
    "CH3COOH": "acetic acid",
    "C2H4": "ethylene",
    "C2H6": "ethane",
    "H2": "hydrogen",
    "O3": "ozone",
    "Cl2": "chlorine",
    "HCl": "hydrochloric acid",
    "H2SO4": "sulfuric acid",
    "HNO3": "nitric acid",
    "CO": "carbon monoxide",
    "H2S": "hydrogen sulfide",
    "N2O": "nitrous oxide",
    "NO2": "nitrogen dioxide",
    "SO2": "sulfur dioxide",
    "H2O2": "hydrogen peroxide",
    "HF": "hydrofluoric acid",
    "CH3OH": "methanol",
    "C2H5Cl": "ethyl chloride",
    "C2H4Cl2": "ethylene dichloride",
    "C2H3Cl": "vinyl chloride",
    "C2H4O": "acetaldehyde",
    "C3H8": "propane",
    "C3H6": "propylene",
    "C4H10": "butane",
    "C4H8": "butylene",
    "C5H12": "pentane",
    "C6H14": "hexane",
    "C7H16": "heptane",
    "C8H18": "octane",
    "C9H20": "nonane",
    "C10H22": "decane",
    "C11H24": "undecane",
    "C12H26": "dodecane",
    "C13H28": "tridecane",
    "C14H30": "tetradecane",
    "C15H32": "pentadecane",
    "C16H34": "hexadecane",
    "C17H36": "heptadecane",
    "C18H38": "octadecane",
    "C19H40": "nonadecane",
    "C20H42": "eicosane",
    "C21H44": "heneicosane",
    "C22H46": "docosane",
    "C23H48": "tricosane",
    "C24H50": "tetracosane",
    "C25H52": "pentacosane",
    "C26H54": "hexacosane",
    "C27H56": "heptacosane",
    "C28H58": "octacosane",
    "C29H60": "nonacosane",
    "C30H62": "triacontane",
    "C40H82": "tetratetracontane",
    "C50H102": "pentacontane",
    "C60H122": "hexacontane",
    "C70H142": "heptacontane",
    "C80H162": "octacontane",
    "C90H182": "nonacontane",
    "C100H202": "hectacontane",
    "CHCl3": "chloroform",
    "CCl4": "carbon tetrachloride",
    "C6H5CN": "benzonitrile",
    "C6H5NO2": "nitrobenzene",
    "C6H6O": "phenol",
    "C6H5CH2OH": "benzyl alcohol",
    "C6H5CH2Cl": "benzyl chloride",
    "C6H5COOH": "benzoic acid",
    "C6H4O2": "benzoquinone",
    "C6H5NH2": "aniline",
    "C6H5NHCOCH3": "acetanilide",
    "C6H5COOC2H5": "ethyl benzoate",
    "C6H5NO": "nitrosobenzene",
    "C6H5NHNH2": "phenylhydrazine",
    "C6H5NHNHC6H5": "diphenylhydrazine",
    "C6H5N(CH3)2": "dimethylaniline"
}

def make_periodic_table():
    elements = {}
    for element in periodic_table_list:
        symbol = element[0]
        name = element[1]
        atomic_mass = element[2]
        elements[symbol] = [name, atomic_mass]  # Using symbol as key and tuple (name, atomic_mass) as value
    return elements

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.

    # Return the total molar mass.
    molar_mass=0
    for i in symbol_quantity_list:
        symbol = i[0]
        quantity = i[1]
        if symbol in periodic_table_dict:
            element = periodic_table_dict[symbol]
            atomic_mass = element[1]
            element_mass = atomic_mass * quantity
            molar_mass += element_mass
    return molar_mass 

def mole_quantity(molar_mass,grams):
    num_moles = grams / molar_mass
    return num_moles

def get_formula_name(formula, known_molecules_dict):
    if formula in known_molecules_dict:
        name = known_molecules_dict[formula]
    return name

def main():
    # Get a chemical formula for a molecule from the user.
    molecule = input("What is the chemical formula? ")
    # Get the mass of a chemical sample in grams from the user.
    mass = float(input("What is the mass in grams of the sample? "))
    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table_dict = make_periodic_table()
    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    parsed_formula = parse_formula(molecule,periodic_table_dict)
    #for element in periodic_table_data: 
    #    print( element[1], element[2])
    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(parsed_formula,periodic_table_dict)
    # Compute the number of moles in the sample.
    number_of_moles = mole_quantity(molar_mass,mass)
    #check against the known formula dictionary, and print the molecule name if included in dictionary.
    name = get_formula_name(molecule,known_molecules_dict)
    #if name is not in the dictionary, ask the user for the name of the molecule and add to the dictionary.
    if name is not None:
        print(f"The name of this molecule is {name}.")
    # Print the molar mass.
    print(f"The molar mass of this molecule is {molar_mass}.")
    # Print the number of moles.
    print(f"There are {number_of_moles} moles in your sample.")

    name = get_formula_name(molecule,known_molecules_dict)
    if name is not None:
        print(f"The name of this molecule is {name}.")
    if name not in known_molecules_dict:
        name = input("I don't know that formula. What is the name of this molecule? ")
        known_molecules_dict[molecule] = f"{name}"


if __name__ == "__main__":
    main()
