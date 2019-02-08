
Execute [demo].[Northwind_Invoices_Pull_MyName]
     @CompanyName = 'market'
    ,@ContactName = ''
    ,@CustomerID = ''
    ,@IncludePaid = ''
    ,@Interject_RequestContext = '<?xml version="1.0" encoding="utf-16" standalone="yes"?>
<RequestContext>
    <ExcelVersion>16.0</ExcelVersion>
    <IdsVersion>2.3.0.11</IdsVersion>
    <FileName>Interject_CustomerDemo_v1.xlsx</FileName>
    <FilePath>C:\Users\MaryM\AppData\Local\Interject\FileCache</FilePath>
    <TabName>CustomerAgingDetail</TabName>
    <CellRange>H27</CellRange>
    <SourceFunction>Ranges</SourceFunction>
    <UtcOffset>-7</UtcOffset>
    <ColDefItems>
        <Value Row="2" Column="1">
            <Name>CustomerId</Name>
        </Value>
        <Value Row="2" Column="2">
            <Name>InvoiceID</Name>
        </Value>
        <Value Row="2" Column="9">
            <Name>InvoiceNum</Name>
        </Value>
        <Value Row="2" Column="10">
            <Name>OrderID</Name>
        </Value>
        <Value Row="2" Column="11">
            <Name>InvoiceDate</Name>
        </Value>
        <Value Row="2" Column="12">
            <Name>Current</Name>
        </Value>
        <Value Row="2" Column="13">
            <Name>30Days</Name>
        </Value>
        <Value Row="2" Column="14">
            <Name>60Days</Name>
        </Value>
        <Value Row="2" Column="15">
            <Name>90Days</Name>
        </Value>
        <Value Row="2" Column="18">
            <Name>ExpectedDate</Name>
        </Value>
        <Value Row="2" Column="20">
            <Name>Note</Name>
        </Value>
        <Value Row="2" Column="21">
            <Name>[Clear]</Name>
        </Value>
    </ColDefItems>
    <ResultDefItems />
    <RowDefItems>
        <Value Row="46" Column="1" ColumnName="CustomerId">
            <Name>BOTTM</Name>
        </Value>
        <Value Row="53" Column="1" ColumnName="CustomerId">
            <Name>BOTTM</Name>
        </Value>
        <Value Row="60" Column="1" ColumnName="CustomerId">
            <Name>BOTTM</Name>
        </Value>
        <Value Row="67" Column="1" ColumnName="CustomerId">
            <Name>BOTTM</Name>
        </Value>
        <Value Row="74" Column="1" ColumnName="CustomerId">
            <Name>GREAL</Name>
        </Value>
        <Value Row="81" Column="1" ColumnName="CustomerId">
            <Name>GREAL</Name>
        </Value>
        <Value Row="88" Column="1" ColumnName="CustomerId">
            <Name>GREAL</Name>
        </Value>
        <Value Row="95" Column="1" ColumnName="CustomerId">
            <Name>GREAL</Name>
        </Value>
        <Value Row="102" Column="1" ColumnName="CustomerId">
            <Name>SAVEA</Name>
        </Value>
        <Value Row="109" Column="1" ColumnName="CustomerId">
            <Name>SAVEA</Name>
        </Value>
        <Value Row="116" Column="1" ColumnName="CustomerId">
            <Name>SAVEA</Name>
        </Value>
        <Value Row="123" Column="1" ColumnName="CustomerId">
            <Name>SAVEA</Name>
        </Value>
        <Value Row="130" Column="1" ColumnName="CustomerId">
            <Name>WHITC</Name>
        </Value>
        <Value Row="137" Column="1" ColumnName="CustomerId">
            <Name>WHITC</Name>
        </Value>
        <Value Row="144" Column="1" ColumnName="CustomerId">
            <Name>WHITC</Name>
        </Value>
        <Value Row="151" Column="1" ColumnName="CustomerId">
            <Name>WHITC</Name>
        </Value>
    </RowDefItems>
    <UserContext>
    <MachineLoginName>MaryM</MachineLoginName>
    <MachineName>.</MachineName>
    <FullName> </FullName>
    <UserId>UUvP4HYoeu</UserId>
    <ClientId>CgCfW9qi</ClientId>
    <LoginName>MaryM@mycompany.com</LoginName>
    <LoginAuthTypeId>10</LoginAuthTypeId>
    <LoginDateUtc>05/03/2018 5:39:48</LoginDateUtc>
    <UserRoles>
        <Role>ClientAdmin</Role>
    </UserRoles>
</UserContext>
    <UserContextEncrypted>Encrypted only through interject api protocol, not direct connection</UserContextEncrypted>
    <XMLDataToSave></XMLDataToSave>
</RequestContext>'