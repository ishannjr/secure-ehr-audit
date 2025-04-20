// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AuditLog {
    struct AuditRecord {
        uint timestamp;
        string patientId;
        string userId;
        string action;
    }

    AuditRecord[] public records;

    event RecordAdded(uint timestamp, string patientId, string userId, string action);

    function addRecord(string memory _patientId, string memory _userId, string memory _action) public {
        records.push(AuditRecord(block.timestamp, _patientId, _userId, _action));
        emit RecordAdded(block.timestamp, _patientId, _userId, _action);
    }

    function getRecord(uint index) public view returns (uint, string memory, string memory, string memory) {
        AuditRecord memory rec = records[index];
        return (rec.timestamp, rec.patientId, rec.userId, rec.action);
    }

    function getRecordCount() public view returns (uint) {
        return records.length;
    }
}