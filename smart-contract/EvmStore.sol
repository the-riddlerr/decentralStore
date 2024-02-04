// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 * @custom:dev-run-script ./scripts/deploy_with_ethers.ts
 */
contract EvmStorage {
    struct Data {
        string description;
        uint256 amount;
    }
    mapping (uint256 => Data) public evmstore;
    uint256 public numberOfEntries;
    event DataStored(uint256 indexed amount, string indexed description);

    function storeData(uint256 amount, string memory description) external {
        evmstore[numberOfEntries].description = description;
        evmstore[numberOfEntries].amount = amount;
        ++numberOfEntries;
        emit DataStored(amount, description);
    }
    function retrieveData() external view returns (Data[] memory) {
        Data[] memory data = new Data[](numberOfEntries);
        for(uint i = 0; i < numberOfEntries; ++i) {
            data[i] = evmstore[i];
        }
        return data;
    }
}
