const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const PROTO_PATH = "./proto/test.proto";
const loaderOptions = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
};

// Initializing the package definition
var packageDef = protoLoader.loadSync(PROTO_PATH, loaderOptions);

const grpcObj = grpc.loadPackageDefinition(packageDef);
// Create server instance
const ourServer = new grpc.Server();

/**
 * grpcObj es un objeto que contiene todos los servicios definidos en el archivo proto.
 *
 * grpcObj.CountryService <-- El nombre del servicio que definimos en el archivo .proto.
 *
 * grpcObj.CountryService.service <-- El servicio en sí.
 */
ourServer.addService(grpcObj.CountryService.service, {
  /**
  * Hay que implementar cada método del servicio que declaramos en el archivo .proto.
  * 
  * @example
  * ```
  * service CountryService {
        rpc GetList(Empty) returns (CountryListResponse);
        rpc UpdateCountry(CountryDTO) returns(Empty);
    }
  * ```
    
  */
  /**
  * Debe retornar el siguiente objeto:
  * ```	
  * {
  *     countries: [
  *         int64 idCountry = 1;
            int64 idRegion = 2;
            string countryName = 3;
            string regionName = 4;
            string countryCodeMain = 5;
            int64 nationalDay = 6
        ]
  * }
    ```
  */
  GetList(request, callback) {
    // El callback debe retornar un objeto con la estructura definida en el archivo .proto
    // Es la respuesta que se le envía al cliente.
    // En este caso, el método GetList retorna un objeto CountryListResponse definido en test.proto.
    callback(null, {
      countries: [
        {
          idCountry: 1,
          idRegion: 1,
          countryName: "Argentina",
          regionName: "America",
          countryCodeMain: "AR",
          nationalDay: 1,
        },
        {
          idCountry: 2,
          idRegion: 1,
          countryName: "Brasil",
          regionName: "America",
          countryCodeMain: "BR",
          nationalDay: 2,
        },
      ],
    });
  },
});

// Bind the server to the port
ourServer.bindAsync(
  "127.0.0.1:50051",
  grpc.ServerCredentials.createInsecure(),
  (error, port) => {
    if (error) console.log(error);
    console.log("Server running at http://127.0.0.1:50051");
    ourServer.start();
  }
);
