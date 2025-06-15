##Exercise: 1 
##Check if the folder exists, if not create one 
##with user input. 
#import os 
##Check if the file exists or not 
#dir_name = input("Enter the folder's name: ") 
##printing the absolute path 
#print("Printing the absolute path: ", os.path.abspath(dir_name)) 
#
#if not os.path.exists(dir_name):
#    rename_dir = input("Name the Folder: ") 
#    os.makedirs(rename_dir) 
#    print("There is no folder named {}.".format(dir_name))
#    print("The folder has been created as {}.".format(rename_dir)) 
#else: 
#    print("The folder already exists.") 

# 
# #Exercise: 2 
# #Unzip a folder  
# import zipfile 
# extract_from = input("Folder Name to Extract from: ")
# extract_to = input("Folder Name to Extract to: ") 
# 
# with zipfile.ZipFile(extract_from, 'r') as archive:
#     archive.extractall(extract_to) 
#     print("The folder has been extracted to {}.".format(extract_to)) 


########################################### 
import os
import zipfile

def is_safe_path(base_dir, target_path):
    """
    Prevent Zip Slip: Ensure extracted path is within target directory.
    """
    return os.path.abspath(target_path).startswith(os.path.abspath(base_dir))

def is_safe_filetype(filename):
    """
    Prevent extraction of dangerous file types.
    """
    dangerous_exts = {'.exe', '.bat', '.cmd', '.js', '.vbs', '.ps1', '.scr', '.dll'}
    return os.path.splitext(filename)[1].lower() not in dangerous_exts

def safe_extract_zip(zip_path, extract_to, max_file_size=100 * 1024 * 1024):  # 100MB limit
    if not os.path.exists(zip_path) or not zipfile.is_zipfile(zip_path):
        raise ValueError("Invalid or corrupted ZIP file.")

    with zipfile.ZipFile(zip_path, 'r') as archive:
        for member in archive.infolist():
            target_path = os.path.join(extract_to, member.filename)

            # 1. Zip Slip protection
            if not is_safe_path(extract_to, target_path):
                raise Exception(f"Blocked unsafe path: {member.filename}")

            # 2. File size check
            if member.file_size > max_file_size:
                raise Exception(f"File too large: {member.filename} ({member.file_size} bytes)")

            # 3. File type check
            if not is_safe_filetype(member.filename):
                print(f"Skipped potentially unsafe file: {member.filename}")
                continue

            # 4. Extraction (create dirs if needed)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            if not member.is_dir():
                with archive.open(member) as source, open(target_path, 'wb') as target:
                    target.write(source.read())

    print(f"✅ The folder has been safely extracted to: {extract_to}")

# === Entry Point ===
try:
    extract_from = input("Folder name to extract from (.zip): ").strip()
    extract_to = input("Folder name to extract to: ").strip()
    safe_extract_zip(extract_from, extract_to)
except Exception as e:
    print(f"❌ Error: {e}")

