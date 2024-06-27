authorize = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string"
                },
                "id": {
                    "type": "string"
                },
                "attributes": {
                    "type": "object",
                    "properties": {
                        "isNewUser": {
                            "type": "boolean"
                        },
                        "email": {
                            "type": "string"
                        },
                        "userId": {
                            "type": "string"
                        },
                        "uuid": {
                            "type": "string"
                        },
                        "xid": {
                            "type": "string"
                        },
                        "hasLinkedLoyaltyCard": {
                            "type": "boolean"
                        },
                        "dyHashedEmail": {
                            "type": "string"
                        }
                    }
                }
            },
            "required": [
                "type",
                "id",
                "attributes"
            ]
        }
    },
    "required": [
        "data"
    ]
}
