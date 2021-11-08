from cerberus import Validator

# バリデーション定義
schema = {
    '生徒ID': {
        'type': 'list',
        'schema': {
            'type': 'string',
            'required': True,
            'empty': False,
            'regex': '^[a-zA-Z][0-9]{5}$',
        }
    },
    '国語点数': {
        'type': 'list',
        'schema': {
            'type': 'integer',
            'min': 0,
            'max': 100
        }
    },
    '数学点数': {
        'type': 'list',
        'schema': {
            'type': 'integer',
            'min': 0,
            'max': 100
        }
    },
    '英語点数': {
        'type': 'list',
        'schema': {
            'type': 'integer',
            'min': 0,
            'max': 200
        }
    }
}

def exec(data) :
    # バリデータを作成
    v = Validator(schema)
    bool = v.validate(data)
    err = v.errors
    return bool, err
