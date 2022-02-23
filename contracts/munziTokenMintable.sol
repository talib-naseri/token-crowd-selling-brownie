pragma solidity ^0.5.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20Detailed.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20Mintable.sol";

contract MUNTokenMintable is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(uint256 initialSupply)
        public
        ERC20Detailed("Munzi", "MUN", 18)
    {
        _mint(msg.sender, initialSupply);
    }
}
