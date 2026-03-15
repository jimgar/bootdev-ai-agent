import os

def get_files_info(working_directory, directory="."):
    try:
        abs_path_wd = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path_wd, directory))

        if not os.path.isdir(target_dir):
            raise f'Error: "{directory}" is not a directory'

        valid_target_dir = os.path.commonpath([abs_path_wd, target_dir]) == abs_path_wd
        if not valid_target_dir:
            raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        items = os.listdir(target_dir)
        items_info = []
        for item in items:
            item_path = os.path.join(target_dir, item)
            item_info = f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            items_info.append(item_info)

        return "\n".join(items_info)
    except Exception as e:
        return f"Error: {e}"


