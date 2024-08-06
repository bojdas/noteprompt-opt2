# generate from py; bojdas
import random
import itertools
import re

# Define the ranges and values for the variables
ages = range(10, 111)
sexes = ["male", "female", "non-binary", "other"]
races = ["White", "Black", "Asiatic", "other"]


def get_tuples():
    pattern = r'\d+\.\s*(.+)'

    symptoms = """
    1.   Rash
	2.	Photosensitivity
	3.	Sleep Disturbances
	4.	Fatigue
	5.	Memory Loss
	6.	Muscle Weakness
	7.	Headaches
	8.	Mood Swings
	9.	Dizziness
	10.	Confusion
	11.	Tremor
	12.	Difficulty Speaking
	13.	Nausea
	14.	Aggression
	15.	Visual Disturbances
	16.	Palpitations
	17.	Sweating
	18.	Weight Loss
	19.	Weight gain
	20.	Hearing Loss
	21.	Back Pain
	22.	Chest Pain
	23.	Joint Pain
	24.	Auditory Hallucinations
	25.	Visual Hallucinations	
    """
    
    symptom_list = re.findall(pattern, symptoms)

    comorbidities = """
    1.	Eczema
	2.	Lupus
	3.	Insomnia
	4.	Chronic Fatigue Syndrome
	5.	Alzheimer’s Disease
	6.	Multiple Sclerosis
	7.	Migraines
	8.	Bipolar Disorder
	9.	Benign paroxysmal positional vertigo
	10.	Reactive Hypoglycemia
	11.	Essential Tremor
	12.	Aphasia
	13.	Gastrointestinal reflux disease
	14.	Intermittent Explosive Disorder
	15.	Glaucoma
	16.	Arrhythmia
	17.	Hyperhidrosis
	18.	Hyperthyroidism
	19.	Hypothyroidism
	20.	Meniere’s Disease
	21.	Herniated Disc
	22.	Angina
	23.	Rheumatoid Arthritis
	24.	Schizophrenia
	25.	Drug Abuse
    """

    comorbidities_list = re.findall(pattern, comorbidities)

    tuples_list = list(zip(symptom_list, comorbidities_list))

    # random_tuple = random.choice(tuples_list)

    # print("TUPLE returned :: ", random_tuple)

    return tuples_list





T = get_tuples()

# Define the values for L, CI, and CO
L = ["value1L", "value2L"]
CI = ["value1CI", "value2CI"]
CO = ["value1CO", "value2CO"]

# Generate all combinations of L, CI, and CO
combinations = list(itertools.product(L, CI, CO))

# Function to generate the sentence
def generate_prompt(X, Y, Z, A, B, I):
    # prompt = f"Generate a prompt with {X},{Y},{Z} using {A} and {B} and {I}"

    prompt = f"""You are a clinician specializing in epilepsy patients. 
You will generate a clinical note for a patient of {X}, {Y}, {Z} characteristics with Symptoms and Co-morbidities {A} and {B}.

The patient should be such that we should be able to decide on whether to give this patient Cenbomate based on the following sources of information: {I}.

The patient note must include the patient’s first and last names and a patient ID."""

    return prompt


# Generate and print the sentences
for A, B in T:
    for L, CI, CO in combinations:
        X = random.choice(ages)
        Y = random.choice(sexes)
        Z = random.choice(races)
        I = f"{L}, {CI}, {CO}"
        print("================================================================================================")
        prompt = generate_prompt(X, Y, Z, A, B, I)
        print(prompt)


