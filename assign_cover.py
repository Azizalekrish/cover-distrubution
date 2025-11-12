import pandas as pd

def assign_covers(teachers_file, covers_file):
    teachers = pd.read_excel(teachers_file)
    covers = pd.read_excel(covers_file)
    
    # Simple round-robin assignment (example)
    covers['Cover Teacher'] = teachers['Name'].sample(len(covers), replace=True).values
    return covers
