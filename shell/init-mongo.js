

const adminDb = db.getSiblingDB("admin");
const databases = adminDb.runCommand({ listDatabases: 1 }).databases;
const dbExists = databases.some(database => database.name === "store_tp");

if (dbExists) {
    quit()
}


// init-mongo.js
db = db.getSiblingDB("store_tp");

// Define schema for the product collection with embedded sales data
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


db.client.insertMany([
    {
        _id: 1,
        name: "Alice Dupont",
        email: "alice.dupont@example.com",
        city: "Paris"
    },
    {
        _id: 2,
        name: "Bob Martin",
        email: "bob.martin@example.com",
        city: "Lyon"
    },
    {
        _id: 3,
        name: "Charlie Bernard",
        email: "charlie.bernard@example.com",
        city: "Marseille"
    }
]);


db.product.insertMany([
    {
        name: "P4-Evo",
        price: 800,
        sales: [
            { date: "2024-09-10", quantity: 25, client_id: 1 }  // Updated to string format
        ]
    },
    {
        name: "P4-Dim3000",
        price: 630,
        sales: [
            { date: "2024-09-12", quantity: 12, client_id: 1 }  // Updated to string format
        ]
    },
    {
        name: "Photoshop Elt",
        price: 94,
        sales: [
            { date: "2024-09-14", quantity: 5, client_id: 2 }  // Updated to string format
        ]
    },
    {
        name: "Encarta",
        price: 21,
        sales: [
            { date: "2024-09-16", quantity: 20, client_id: 3 }  // Updated to string format
        ]
    },
    {
        name: "Office 2003",
        price: 455,
        sales: [
            { date: "2024-09-18", quantity: 20, client_id: 2 }  // Updated to string format
        ]
    },
    {
        name: "DreamWeaver",
        price: 130,
        sales: [
            { date: "2024-09-20", quantity: 15, client_id: 1 }  // Updated to string format
        ]
    },
    {
        name: "C++ Builder",
        price: 54,
        sales: [
            { date: "2024-09-22", quantity: 5, client_id: 1 }  // Updated to string format
        ]
    }
]);
