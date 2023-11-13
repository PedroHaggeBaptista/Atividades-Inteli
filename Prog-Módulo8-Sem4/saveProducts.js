const PrismaClient = require('@prisma/client').PrismaClient;

const prisma = new PrismaClient();

async function saveProduct(name) {
    await prisma.product.create({
        data: {
            name: name
        }
    })

    return "Saved"
}

for (i=0; i < 10000; i++) {
    saveProduct("Product " + i)
        .then((res) => {
            console.log(res)
        })
        .catch((err) => {
            console.log(err)
        })
}