from argparse import ArgumentParser
import sys
from pathlib import Path
import pickle
import json
import describe


if __name__ == '__main__':
    parser = ArgumentParser()
    # no name_or_flags are required, to receive the filename
    parser.add_argument('file')
    parser.add_argument('--no-pickle-import', action='store_true', default=False,
                        help='Do NOT import third-party modules to read pickle file. '
                             'e.g. import numpy to read `numpy.ndarray` objects.')
    # parser.add_argument('-n', '--length-of-container', default=10,
    #                     )

    args = parser.parse_args()

    # switch by file extensions
    args.file = Path(args.file)

    if args.file.suffix == '.pkl':
        with args.file.open('rb') as f:
            obj = pickle.load(f)
    elif args.file.suffix == '.json':
        with args.file.open('r', encoding='utf-8') as f:
            obj = json.load(f)

    desc = describe.desc_obj(obj)

    to_save_p = args.file.with_name('_desc_' + args.file.stem + '.json')
    with to_save_p.open('w', encoding='utf-8') as f:
        json.dump(desc, f, ensure_ascii=False, indent=4)