# Schema `Product` & `Client`

1. `Product` et son schema de validation (name, price et sales).
    - `sales` est un 'embedded' schema qui stock tout les vents d'un produit, avec l'id du client associé. 
2. `Client` qui contient les informations personel 

```json
    db.createCollection("product", {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                required: ["name", "price", "sales"],
                properties: {
                    name: {
                        bsonType: "string",
                        description: "must be a string and is required"
                    },
                    price: {
                        bsonType: "number",
                        description: "must be a number and is required"
                    },
                    sales: {
                        bsonType: "array",
                        items: {
                            bsonType: "object",
                            required: ["date", "quantity", "client_id"],
                            properties: {
                                date: {
                                    bsonType: "string",
                                    description: "must be a string and is required"
                                },
                                quantity: {
                                    bsonType: "number",
                                    description: "must be a number and is required"
                                },
                                client_id: {
                                    bsonType: "int",
                                    description: "must be an integer and is required"
                                }
                            }
                        },
                        description: "must be an array of sales objects and is required"
                    }
                }
            }
        }
    });

    // Define schema for the client collection
    db.createCollection("client", {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                required: ["name", "email"],
                properties: {
                    name: {
                        bsonType: "string",
                        description: "must be a string and is required"
                    },
                    email: {
                        bsonType: "string",
                        pattern: "^.+@.+$",
                        description: "must be a string and match the email pattern"
                    }
                }
            }
        }
    });
```