const contractAddress = "0x0aAb38709774593d1641a7F902022Be729Be9986";
const abi = [
  {
    inputs: [
      {
        internalType: "int256",
        name: "packageid",
        type: "int256",
      },
      {
        internalType: "string",
        name: "initlocation",
        type: "string",
      },
      {
        internalType: "string",
        name: "action",
        type: "string",
      },
      {
        internalType: "string",
        name: "undertaken",
        type: "string",
      },
    ],
    name: "addpackage",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "int256",
        name: "packageid",
        type: "int256",
      },
    ],
    name: "getpackage",
    outputs: [
      {
        internalType: "string",
        name: "",
        type: "string",
      },
      {
        internalType: "string",
        name: "",
        type: "string",
      },
      {
        internalType: "string",
        name: "",
        type: "string",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
];
if (typeof window.ethereum === "undefined") {
  throw new Error("MetaMask is not installed or not properly configured");
}
const web3 = new Web3(window.ethereum);
const contract = new web3.eth.Contract(abi, contractAddress);
(async () => {
  document
    .getElementById("connectButton")
    .addEventListener("click", async () => {
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        await window.ethereum.request({ method: "eth_requestAccounts" });
        const accounts = await web3.eth.getAccounts();
        document.getElementById(
          "connectButton"
        ).innerText = `Connected: ${accounts[0].slice(
          0,
          6
        )}...${accounts[0].slice(-4)}`;
        document
          .getElementById("contract-interaction")
          .classList.remove("visually-hidden");
        document
          .getElementById("connect-to-metamask")
          .classList.add("visually-hidden");
      } else {
        alert("Please download Metamask");
      }
    });
  const addPackageForm = document.getElementById("addPackageForm");
  addPackageForm.addEventListener("submit", async (e) => {
    try {
      e.preventDefault();
      const formData = new FormData(addPackageForm);
      const packageid = formData.get("packageid");
      const initloc = formData.get("initloc");
      const action = formData.get("action");
      const undertaken = formData.get("undertaken");
      const accounts = await window.ethereum.request({
        method: "eth_requestAccounts",
      });
      const contractFunction = {
        inputs: [
          {
            internalType: "int256",
            name: "packageid",
            type: "int256",
          },
          {
            internalType: "string",
            name: "initlocation",
            type: "string",
          },
          {
            internalType: "string",
            name: "action",
            type: "string",
          },
          {
            internalType: "string",
            name: "undertaken",
            type: "string",
          },
        ],
        name: "addpackage",
        outputs: [],
        stateMutability: "nonpayable",
        type: "function",
      };
      const functionArguments = [packageid, initloc, action, undertaken];
      const encodedData = web3.eth.abi.encodeFunctionCall(
        contractFunction,
        functionArguments
      );
      const rawTransaction = {
        from: accounts[0],
        to: contractAddress,
        value: 0,
        maxFeePerGas: (await web3.eth.getBlock()).baseFeePerGas * 2n,
        maxPriorityFeePerGas: 500,
        gasLimit: 2000000,
        nonce: await web3.eth.getTransactionCount(accounts[0]),
        data: encodedData,
      };
      const tx = await web3.eth.sendTransaction(rawTransaction);
      console.log(tx);
      if (tx) {
        const addPackageBtn = document.getElementById("addPackage");
        const span = addPackageBtn.querySelector("span");
        span.classList.add("visually-hidden");
      }
    } catch (err) {
      console.log(err);
    }
  });
  const getPackageForm = document.getElementById("getPackageForm");
  getPackageForm.addEventListener("submit", async (e) => {
    try {
      e.preventDefault();
      const formData = new FormData(getPackageForm);
      const packageid = formData.get("packageid");
      const packageDetails = await contract.methods
        .getpackage(packageid)
        .call();
      console.log(packageDetails);
      if (packageDetails) {
        const getPackageBtn = document.getElementById("getPackage");
        const span = getPackageBtn.querySelector("span");
        span.classList.add("visually-hidden");
      }
      const { 0: initloc, 1: action, 2: undertaken } = packageDetails;
      document.getElementById("packageIdSpan").innerText = packageid;
      document.getElementById("initLocSpan").innerText = initloc;
      document.getElementById("actionSpan").innerText = action;
      document.getElementById("undertakenSpan").innerText = undertaken;
    } catch (err) {
      console.log(err);
    }
  });
})();