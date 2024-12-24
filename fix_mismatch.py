import os


def fix_file_mismatch(data_dir, text_file, label_file):
    text_path = os.path.join(data_dir, text_file)
    label_path = os.path.join(data_dir, label_file)

    with open(text_path, 'r') as tf, open(label_path, 'r') as lf:
        text_lines = tf.read().splitlines()
        label_lines = lf.read().splitlines()

    if len(text_lines) != len(label_lines):
        print(
            f"Mismatch found: {text_file} has {len(text_lines)} lines, but {label_file} has {len(label_lines)} lines.")

        # Identify the mismatched lines
        min_len = min(len(text_lines), len(label_lines))
        for i in range(min_len):
            if text_lines[i] != label_lines[i]:
                print(f"Mismatch at line {i + 1}:")
                print(f"  {text_file}: {text_lines[i]}")
                print(f"  {label_file}: {label_lines[i]}")

        # Fix the mismatch by truncating the longer file
        if len(text_lines) > len(label_lines):
            text_lines = text_lines[:len(label_lines)]
        else:
            label_lines = label_lines[:len(text_lines)]

        # Write the fixed lines back to the files
        with open(text_path, 'w') as tf:
            tf.write('\n'.join(text_lines) + '\n')
        with open(label_path, 'w') as lf:
            lf.write('\n'.join(label_lines) + '\n')

        print(f"Files have been fixed: {text_file} and {label_file} now have the same number of lines.")
    else:
        print(f"No mismatch: {text_file} and {label_file} have the same number of lines.")


if __name__ == "__main__":
    data_dir = 'resume-corpus'
    train_file = 'train.txt'
    train_label_file = 'train.lab'
    val_file = 'val.txt'
    val_label_file = 'val.lab'

    fix_file_mismatch(data_dir, train_file, train_label_file)
    fix_file_mismatch(data_dir, val_file, val_label_file)
