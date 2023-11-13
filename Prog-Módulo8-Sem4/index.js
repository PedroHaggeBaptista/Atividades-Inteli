const redis = require("redis");

const { PrismaClient } = require("@prisma/client");

const prisma = new PrismaClient();

let redisClient;

(async () => {
  redisClient = redis.createClient();

  redisClient.on("error", (error) => console.error(`Error : ${error}`));

  await redisClient.connect();
})();

async function getProducts(id) {
  const productId = id;
  const cacheResults = await redisClient.get(`produtos:${productId}`);
  console.log({ dados: cacheResults });
  return { dados: cacheResults };
}

async function setProducts(id, name) {
  const productId = id;

  redisClient.set(`produtos:${productId}`, name);

  redisClient.expireAt(
    `produtos:${productId}`,
    parseInt(+new Date() / 1000) + 86400
  );

  console.log("Saved");
}

async function verifyProduct(id) {
  //Verify if product exists in cache
  const cacheResults = await getProducts(id);

  if (cacheResults.dados != null) {
    return cacheResults.dados;
  }

  //Verify if product exists in database
  const product = await prisma.product.findFirst({
    where: {
      id: id,
    },
  });

  if (product != null) {
    //Save product in cache
    setProducts(id, product.name);

    return product.name;
  } else {
    return "Produto não encontrado na base de dados";
  }
}

async function run(id) {
  let startDate = new Date();
  console.log(await verifyProduct(id));
  let endDate = new Date();

  console.log("Tempo de execução: " + (endDate - startDate) + "ms");

  redisClient.quit();
}

run(1);