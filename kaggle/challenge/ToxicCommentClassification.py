import os

_prefix = ['~', '.ml', 'kaggle', 'challenge', 'ToxicCommentClassification']


def filepath(path: str):
    return os.path.join(*_prefix, path)


train_filename = 'train.csv'
test_filename = 'test.csv'
train_filepath = filepath(train_filename)
test_filepath = filepath(test_filename)


__all__ = ['train_filename', 'train_filepath', 'test_filename', 'test_filepath', 'filepath', ]

if __name__ == '__main__':
    print(train_filepath)
    print(test_filepath)
    print(filepath('my.csv'))
