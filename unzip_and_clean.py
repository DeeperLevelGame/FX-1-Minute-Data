import os
import zipfile

# Define the base paths
input_folder = r"output"
output_folder = r"output_unzipped"

# Loop through all subfolders in the input folder
for subdir in os.listdir(input_folder):
    subdir_path = os.path.join(input_folder, subdir)

    if os.path.isdir(subdir_path):
        print(f"Processing folder: {subdir}")

        # Create the corresponding output_unzipped folder
        output_subdir = os.path.join(output_folder, subdir)
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        # Loop through all .zip files in the current subfolder
        for root, _, files in os.walk(subdir_path):
            for file in files:
                if file.endswith(".zip"):
                    zip_file_path = os.path.join(root, file)
                    print(f"Unzipping: {zip_file_path}")

                    # Unzip the file
                    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                        zip_ref.extractall(output_subdir)

        # Delete all .txt files in the output_unzipped folder
        print(f"Deleting .txt files in: {output_subdir}")
        for root, _, files in os.walk(output_subdir):
            for file in files:
                if file.endswith(".txt"):
                    txt_file_path = os.path.join(root, file)
                    os.remove(txt_file_path)
                    print(f"Deleted: {txt_file_path}")

print("Process completed.")
