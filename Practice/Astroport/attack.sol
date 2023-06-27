pragma solidity ^0.8.0;

contract Test {

    uint256 public constant x_token_total_supply = 10000000;
    uint256 public total_staked_amount = 0;

    constructor(){

    }

    function findNumber(uint256 amount_to_stake) external returns(uint256){
        total_staked_amount += amount_to_stake;
        uint256 toMint = (amount_to_stake * x_token_total_supply) / total_staked_amount; 
        
        //mint x_token to msg.sender

        return toMint;
    }

    /*
        When the contract is at initial state - it just has been deployed - then an attacker can take advantage of the above formula in order to get all the x_token_total_supply for himself by depositing only 1 wei.
        He may use this whole x_token_total_supply to control the DAO associated with the token and also other mints won't be able to go through, since the x_token_total_supply will have reached its maximum.
    */
}