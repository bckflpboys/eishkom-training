import json

def update_nb(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and any('drive.mount' in line for line in cell.get('source', [])):
            cell['source'] = [
                "# 2. Setup workspace: Unzip eishkom_colab_kit.zip (or mount Google Drive)\n",
                "import os, zipfile\n",
                "if os.path.exists('eishkom_colab_kit.zip'):\n",
                "    print('Unpacking eishkom_colab_kit.zip...')\n",
                "    with zipfile.ZipFile('eishkom_colab_kit.zip', 'r') as zip_ref:\n",
                "        zip_ref.extractall('.')\n",
                "    os.environ['SA_WORKSPACE'] = os.path.abspath('workspace')\n",
                "    print('Workspace ready at:', os.environ['SA_WORKSPACE'])\n",
                "    !ls -la workspace/build/r1\n",
                "else:\n",
                "    print('TIP: Drag and drop eishkom_colab_kit.zip into the Files panel on the left!')\n",
                "    try:\n",
                "        from google.colab import drive\n",
                "        drive.mount('/content/drive')\n",
                "        KIT = '/content/drive/MyDrive/sa-tutor-kit'\n",
                "        os.environ['SA_WORKSPACE'] = KIT + '/workspace'\n",
                "        %cd {KIT}\n",
                "        !ls\n",
                "    except Exception as e:\n",
                "        print('Drive mount skipped or unavailable. Please upload eishkom_colab_kit.zip directly.')\n"
            ]
            break

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print(f"Updated {path}")

update_nb('sa_tutor_colab.ipynb')
update_nb('sa-tutor-kit/sa-tutor-kit/colab/sa_tutor_colab.ipynb')

