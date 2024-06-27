search_item = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "model_id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                },
                "slug": {
                    "type": "string"
                },
                "is_buyable": {
                    "type": "boolean"
                },
                "photos": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "small": {
                                    "type": "string"
                                },
                                "middle": {
                                    "type": "string"
                                },
                                "tiny": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "small",
                                "middle",
                                "tiny"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "small": {
                                    "type": "string"
                                },
                                "middle": {
                                    "type": "string"
                                },
                                "tiny": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "small",
                                "middle",
                                "tiny"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "small": {
                                    "type": "string"
                                },
                                "middle": {
                                    "type": "string"
                                },
                                "tiny": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "small",
                                "middle",
                                "tiny"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "small": {
                                    "type": "string"
                                },
                                "middle": {
                                    "type": "string"
                                },
                                "tiny": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "small",
                                "middle",
                                "tiny"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "small": {
                                    "type": "string"
                                },
                                "middle": {
                                    "type": "string"
                                },
                                "tiny": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "small",
                                "middle",
                                "tiny"
                            ]
                        }
                    ]
                },
                "color_code": {
                    "type": "string"
                },
                "colorConcrete": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "content_id": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "slug": {
                            "type": "string"
                        },
                        "hex": {
                            "type": "string"
                        },
                        "feminine": {
                            "type": "string"
                        },
                        "neutral": {
                            "type": "string"
                        },
                        "plural": {
                            "type": "string"
                        },
                        "parental": {
                            "type": "string"
                        },
                        "image_url": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "content_id",
                        "title",
                        "slug",
                        "hex",
                        "feminine",
                        "neutral",
                        "plural",
                        "parental",
                        "image_url"
                    ]
                },
                "skuList": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "item_id": {
                                    "type": "integer"
                                },
                                "ext_id": {
                                    "type": "integer"
                                },
                                "ext_guid": {
                                    "type": "string"
                                },
                                "barcode": {
                                    "type": "string"
                                },
                                "barcode_vnd": {
                                    "type": "string"
                                },
                                "season": {
                                    "type": "string"
                                },
                                "size_id": {
                                    "type": "integer"
                                },
                                "size_vendor_name": {
                                    "type": "string"
                                },
                                "price_original": {
                                    "type": "integer"
                                },
                                "price_discount": {
                                    "type": "integer"
                                },
                                "discount": {
                                    "type": "integer"
                                },
                                "internationalPrice": {
                                    "type": "object",
                                    "properties": {
                                        "base": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        },
                                        "displayed": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "base",
                                        "displayed"
                                    ]
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "is_buyable": {
                                    "type": "integer"
                                },
                                "availabilityInStock": {
                                    "type": "boolean"
                                },
                                "isLast": {
                                    "type": "boolean"
                                },
                                "size": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "title_vnd": {
                                            "type": "string"
                                        },
                                        "visible": {
                                            "type": "integer"
                                        },
                                        "is_visible_in_catalog": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "title_vnd",
                                        "visible",
                                        "is_visible_in_catalog"
                                    ]
                                },
                                "sizeAttributes": {
                                    "type": "object",
                                    "properties": {
                                        "russianLabel": {
                                            "type": "string"
                                        },
                                        "russianSize": {
                                            "type": "string"
                                        },
                                        "vendorLabel": {
                                            "type": "null"
                                        },
                                        "vendorSize": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "russianLabel",
                                        "russianSize",
                                        "vendorLabel",
                                        "vendorSize"
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "item_id",
                                "ext_id",
                                "ext_guid",
                                "barcode",
                                "barcode_vnd",
                                "season",
                                "size_id",
                                "size_vendor_name",
                                "price_original",
                                "price_discount",
                                "discount",
                                "internationalPrice",
                                "visible",
                                "is_buyable",
                                "availabilityInStock",
                                "isLast",
                                "size",
                                "sizeAttributes"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "item_id": {
                                    "type": "integer"
                                },
                                "ext_id": {
                                    "type": "integer"
                                },
                                "ext_guid": {
                                    "type": "string"
                                },
                                "barcode": {
                                    "type": "string"
                                },
                                "barcode_vnd": {
                                    "type": "string"
                                },
                                "season": {
                                    "type": "string"
                                },
                                "size_id": {
                                    "type": "integer"
                                },
                                "size_vendor_name": {
                                    "type": "string"
                                },
                                "price_original": {
                                    "type": "integer"
                                },
                                "price_discount": {
                                    "type": "integer"
                                },
                                "discount": {
                                    "type": "integer"
                                },
                                "internationalPrice": {
                                    "type": "object",
                                    "properties": {
                                        "base": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        },
                                        "displayed": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "base",
                                        "displayed"
                                    ]
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "is_buyable": {
                                    "type": "integer"
                                },
                                "availabilityInStock": {
                                    "type": "boolean"
                                },
                                "isLast": {
                                    "type": "boolean"
                                },
                                "size": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "title_vnd": {
                                            "type": "string"
                                        },
                                        "visible": {
                                            "type": "integer"
                                        },
                                        "is_visible_in_catalog": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "title_vnd",
                                        "visible",
                                        "is_visible_in_catalog"
                                    ]
                                },
                                "sizeAttributes": {
                                    "type": "object",
                                    "properties": {
                                        "russianLabel": {
                                            "type": "string"
                                        },
                                        "russianSize": {
                                            "type": "string"
                                        },
                                        "vendorLabel": {
                                            "type": "null"
                                        },
                                        "vendorSize": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "russianLabel",
                                        "russianSize",
                                        "vendorLabel",
                                        "vendorSize"
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "item_id",
                                "ext_id",
                                "ext_guid",
                                "barcode",
                                "barcode_vnd",
                                "season",
                                "size_id",
                                "size_vendor_name",
                                "price_original",
                                "price_discount",
                                "discount",
                                "internationalPrice",
                                "visible",
                                "is_buyable",
                                "availabilityInStock",
                                "isLast",
                                "size",
                                "sizeAttributes"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "item_id": {
                                    "type": "integer"
                                },
                                "ext_id": {
                                    "type": "integer"
                                },
                                "ext_guid": {
                                    "type": "string"
                                },
                                "barcode": {
                                    "type": "string"
                                },
                                "barcode_vnd": {
                                    "type": "string"
                                },
                                "season": {
                                    "type": "string"
                                },
                                "size_id": {
                                    "type": "integer"
                                },
                                "size_vendor_name": {
                                    "type": "string"
                                },
                                "price_original": {
                                    "type": "integer"
                                },
                                "price_discount": {
                                    "type": "integer"
                                },
                                "discount": {
                                    "type": "integer"
                                },
                                "internationalPrice": {
                                    "type": "object",
                                    "properties": {
                                        "base": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        },
                                        "displayed": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "base",
                                        "displayed"
                                    ]
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "is_buyable": {
                                    "type": "integer"
                                },
                                "availabilityInStock": {
                                    "type": "boolean"
                                },
                                "isLast": {
                                    "type": "boolean"
                                },
                                "size": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "title_vnd": {
                                            "type": "string"
                                        },
                                        "visible": {
                                            "type": "integer"
                                        },
                                        "is_visible_in_catalog": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "title_vnd",
                                        "visible",
                                        "is_visible_in_catalog"
                                    ]
                                },
                                "sizeAttributes": {
                                    "type": "object",
                                    "properties": {
                                        "russianLabel": {
                                            "type": "string"
                                        },
                                        "russianSize": {
                                            "type": "string"
                                        },
                                        "vendorLabel": {
                                            "type": "null"
                                        },
                                        "vendorSize": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "russianLabel",
                                        "russianSize",
                                        "vendorLabel",
                                        "vendorSize"
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "item_id",
                                "ext_id",
                                "ext_guid",
                                "barcode",
                                "barcode_vnd",
                                "season",
                                "size_id",
                                "size_vendor_name",
                                "price_original",
                                "price_discount",
                                "discount",
                                "internationalPrice",
                                "visible",
                                "is_buyable",
                                "availabilityInStock",
                                "isLast",
                                "size",
                                "sizeAttributes"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "item_id": {
                                    "type": "integer"
                                },
                                "ext_id": {
                                    "type": "integer"
                                },
                                "ext_guid": {
                                    "type": "string"
                                },
                                "barcode": {
                                    "type": "string"
                                },
                                "barcode_vnd": {
                                    "type": "string"
                                },
                                "season": {
                                    "type": "string"
                                },
                                "size_id": {
                                    "type": "integer"
                                },
                                "size_vendor_name": {
                                    "type": "string"
                                },
                                "price_original": {
                                    "type": "integer"
                                },
                                "price_discount": {
                                    "type": "integer"
                                },
                                "discount": {
                                    "type": "integer"
                                },
                                "internationalPrice": {
                                    "type": "object",
                                    "properties": {
                                        "base": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        },
                                        "displayed": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "base",
                                        "displayed"
                                    ]
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "is_buyable": {
                                    "type": "integer"
                                },
                                "availabilityInStock": {
                                    "type": "boolean"
                                },
                                "isLast": {
                                    "type": "boolean"
                                },
                                "size": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "title_vnd": {
                                            "type": "string"
                                        },
                                        "visible": {
                                            "type": "integer"
                                        },
                                        "is_visible_in_catalog": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "title_vnd",
                                        "visible",
                                        "is_visible_in_catalog"
                                    ]
                                },
                                "sizeAttributes": {
                                    "type": "object",
                                    "properties": {
                                        "russianLabel": {
                                            "type": "string"
                                        },
                                        "russianSize": {
                                            "type": "string"
                                        },
                                        "vendorLabel": {
                                            "type": "null"
                                        },
                                        "vendorSize": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "russianLabel",
                                        "russianSize",
                                        "vendorLabel",
                                        "vendorSize"
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "item_id",
                                "ext_id",
                                "ext_guid",
                                "barcode",
                                "barcode_vnd",
                                "season",
                                "size_id",
                                "size_vendor_name",
                                "price_original",
                                "price_discount",
                                "discount",
                                "internationalPrice",
                                "visible",
                                "is_buyable",
                                "availabilityInStock",
                                "isLast",
                                "size",
                                "sizeAttributes"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "item_id": {
                                    "type": "integer"
                                },
                                "ext_id": {
                                    "type": "integer"
                                },
                                "ext_guid": {
                                    "type": "string"
                                },
                                "barcode": {
                                    "type": "string"
                                },
                                "barcode_vnd": {
                                    "type": "string"
                                },
                                "season": {
                                    "type": "string"
                                },
                                "size_id": {
                                    "type": "integer"
                                },
                                "size_vendor_name": {
                                    "type": "string"
                                },
                                "price_original": {
                                    "type": "integer"
                                },
                                "price_discount": {
                                    "type": "integer"
                                },
                                "discount": {
                                    "type": "integer"
                                },
                                "internationalPrice": {
                                    "type": "object",
                                    "properties": {
                                        "base": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        },
                                        "displayed": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "base",
                                        "displayed"
                                    ]
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "is_buyable": {
                                    "type": "integer"
                                },
                                "availabilityInStock": {
                                    "type": "boolean"
                                },
                                "isLast": {
                                    "type": "boolean"
                                },
                                "size": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "title_vnd": {
                                            "type": "string"
                                        },
                                        "visible": {
                                            "type": "integer"
                                        },
                                        "is_visible_in_catalog": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "title_vnd",
                                        "visible",
                                        "is_visible_in_catalog"
                                    ]
                                },
                                "sizeAttributes": {
                                    "type": "object",
                                    "properties": {
                                        "russianLabel": {
                                            "type": "string"
                                        },
                                        "russianSize": {
                                            "type": "string"
                                        },
                                        "vendorLabel": {
                                            "type": "null"
                                        },
                                        "vendorSize": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "russianLabel",
                                        "russianSize",
                                        "vendorLabel",
                                        "vendorSize"
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "item_id",
                                "ext_id",
                                "ext_guid",
                                "barcode",
                                "barcode_vnd",
                                "season",
                                "size_id",
                                "size_vendor_name",
                                "price_original",
                                "price_discount",
                                "discount",
                                "internationalPrice",
                                "visible",
                                "is_buyable",
                                "availabilityInStock",
                                "isLast",
                                "size",
                                "sizeAttributes"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "item_id": {
                                    "type": "integer"
                                },
                                "ext_id": {
                                    "type": "integer"
                                },
                                "ext_guid": {
                                    "type": "string"
                                },
                                "barcode": {
                                    "type": "string"
                                },
                                "barcode_vnd": {
                                    "type": "string"
                                },
                                "season": {
                                    "type": "string"
                                },
                                "size_id": {
                                    "type": "integer"
                                },
                                "size_vendor_name": {
                                    "type": "string"
                                },
                                "price_original": {
                                    "type": "integer"
                                },
                                "price_discount": {
                                    "type": "integer"
                                },
                                "discount": {
                                    "type": "integer"
                                },
                                "internationalPrice": {
                                    "type": "object",
                                    "properties": {
                                        "base": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        },
                                        "displayed": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "base",
                                        "displayed"
                                    ]
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "is_buyable": {
                                    "type": "integer"
                                },
                                "availabilityInStock": {
                                    "type": "boolean"
                                },
                                "isLast": {
                                    "type": "boolean"
                                },
                                "size": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "title_vnd": {
                                            "type": "string"
                                        },
                                        "visible": {
                                            "type": "integer"
                                        },
                                        "is_visible_in_catalog": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "title_vnd",
                                        "visible",
                                        "is_visible_in_catalog"
                                    ]
                                },
                                "sizeAttributes": {
                                    "type": "object",
                                    "properties": {
                                        "russianLabel": {
                                            "type": "string"
                                        },
                                        "russianSize": {
                                            "type": "string"
                                        },
                                        "vendorLabel": {
                                            "type": "null"
                                        },
                                        "vendorSize": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "russianLabel",
                                        "russianSize",
                                        "vendorLabel",
                                        "vendorSize"
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "item_id",
                                "ext_id",
                                "ext_guid",
                                "barcode",
                                "barcode_vnd",
                                "season",
                                "size_id",
                                "size_vendor_name",
                                "price_original",
                                "price_discount",
                                "discount",
                                "internationalPrice",
                                "visible",
                                "is_buyable",
                                "availabilityInStock",
                                "isLast",
                                "size",
                                "sizeAttributes"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "item_id": {
                                    "type": "integer"
                                },
                                "ext_id": {
                                    "type": "integer"
                                },
                                "ext_guid": {
                                    "type": "string"
                                },
                                "barcode": {
                                    "type": "string"
                                },
                                "barcode_vnd": {
                                    "type": "string"
                                },
                                "season": {
                                    "type": "string"
                                },
                                "size_id": {
                                    "type": "integer"
                                },
                                "size_vendor_name": {
                                    "type": "string"
                                },
                                "price_original": {
                                    "type": "integer"
                                },
                                "price_discount": {
                                    "type": "integer"
                                },
                                "discount": {
                                    "type": "integer"
                                },
                                "internationalPrice": {
                                    "type": "object",
                                    "properties": {
                                        "base": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        },
                                        "displayed": {
                                            "type": "object",
                                            "properties": {
                                                "original": {
                                                    "type": "integer"
                                                },
                                                "discounted": {
                                                    "type": "integer"
                                                },
                                                "currency": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "original",
                                                "discounted",
                                                "currency"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "base",
                                        "displayed"
                                    ]
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "is_buyable": {
                                    "type": "integer"
                                },
                                "availabilityInStock": {
                                    "type": "boolean"
                                },
                                "isLast": {
                                    "type": "boolean"
                                },
                                "size": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "title_vnd": {
                                            "type": "string"
                                        },
                                        "visible": {
                                            "type": "integer"
                                        },
                                        "is_visible_in_catalog": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "title_vnd",
                                        "visible",
                                        "is_visible_in_catalog"
                                    ]
                                },
                                "sizeAttributes": {
                                    "type": "object",
                                    "properties": {
                                        "russianLabel": {
                                            "type": "string"
                                        },
                                        "russianSize": {
                                            "type": "string"
                                        },
                                        "vendorLabel": {
                                            "type": "null"
                                        },
                                        "vendorSize": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "russianLabel",
                                        "russianSize",
                                        "vendorLabel",
                                        "vendorSize"
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "item_id",
                                "ext_id",
                                "ext_guid",
                                "barcode",
                                "barcode_vnd",
                                "season",
                                "size_id",
                                "size_vendor_name",
                                "price_original",
                                "price_discount",
                                "discount",
                                "internationalPrice",
                                "visible",
                                "is_buyable",
                                "availabilityInStock",
                                "isLast",
                                "size",
                                "sizeAttributes"
                            ]
                        }
                    ]
                },
                "tags": {
                    "type": "array",
                    "items": {}
                },
                "selections": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "string"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "visible": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "slug": {
                                    "type": "string"
                                },
                                "preview_photo_id": {
                                    "type": "null"
                                },
                                "detail_photo_id": {
                                    "type": "null"
                                },
                                "url": {
                                    "type": "null"
                                },
                                "back_url": {
                                    "type": "null"
                                },
                                "item_id": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "id",
                                "visible",
                                "title",
                                "slug",
                                "preview_photo_id",
                                "detail_photo_id",
                                "url",
                                "back_url",
                                "item_id"
                            ]
                        }
                    ]
                },
                "description_lit": {
                    "type": "string"
                },
                "description_seo": {
                    "type": "null"
                },
                "image_alt": {
                    "type": "null"
                },
                "image_title": {
                    "type": "null"
                },
                "ext_id": {
                    "type": "string"
                },
                "gender": {
                    "type": "string"
                },
                "season": {
                    "type": "string"
                },
                "brand_id": {
                    "type": "integer"
                },
                "brand_name": {
                    "type": "string"
                },
                "category_id": {
                    "type": "integer"
                },
                "category_slug": {
                    "type": "string"
                },
                "in_wishlist": {
                    "type": "boolean"
                },
                "has_size_table": {
                    "type": "boolean"
                },
                "looks_availability_in_stock": {
                    "type": "boolean"
                },
                "isLimited": {
                    "type": "boolean"
                },
                "isMercury": {
                    "type": "boolean"
                },
                "brandListLogoUrl": {
                    "type": "string"
                },
                "brandLogoUrl": {
                    "type": "string"
                },
                "brandIosLogoUrl": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "model_id",
                "title",
                "slug",
                "is_buyable",
                "photos",
                "color_code",
                "colorConcrete",
                "skuList",
                "tags",
                "selections",
                "description_lit",
                "description_seo",
                "image_alt",
                "image_title",
                "ext_id",
                "gender",
                "season",
                "brand_id",
                "brand_name",
                "category_id",
                "category_slug",
                "in_wishlist",
                "has_size_table",
                "looks_availability_in_stock",
                "isLimited",
                "isMercury",
                "brandListLogoUrl",
                "brandLogoUrl",
                "brandIosLogoUrl"
            ]
        }
    ]
}
