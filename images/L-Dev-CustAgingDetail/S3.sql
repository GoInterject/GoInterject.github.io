
Execute [demo].[Northwind_CustomerInvoices_Pull_MyName]
    @CompanyName = 'market'
    ,@ContactName = ''
    ,@CustomerID = ''
    ,@IncludePaid = ''
    ,@Interject_RequestContext = '<?xml version="1.0" encoding="utf-16" standalone="yes"?>
<RequestContext>
    <ExcelVersion>16.0</ExcelVersion>
    <IdsVersion>2.3.0.11</IdsVersion>
    <FileName>Interject_CustomerDemo_v1.xlsx</FileName>
    <FilePath>C:\Users\Marym\AppData\Local\Interject\FileCache</FilePath>
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
        <Value Row="61" Column="1" ColumnName="CustomerId">
            <Name>BOTTM</Name>
        </Value>
        <Value Row="76" Column="1" ColumnName="CustomerId">
            <Name>BOTTM</Name>
        </Value>
        <Value Row="91" Column="1" ColumnName="CustomerId">
            <Name>BOTTM</Name>
        </Value>
        <Value Row="106" Column="1" ColumnName="CustomerId">
            <Name>GREAL</Name>
        </Value>
        <Value Row="117" Column="1" ColumnName="CustomerId">
            <Name>GREAL</Name>
        </Value>
        <Value Row="128" Column="1" ColumnName="CustomerId">
            <Name>GREAL</Name>
        </Value>
        <Value Row="139" Column="1" ColumnName="CustomerId">
            <Name>GREAL</Name>
        </Value>
        <Value Row="150" Column="1" ColumnName="CustomerId">
            <Name>SAVEA</Name>
        </Value>
        <Value Row="173" Column="1" ColumnName="CustomerId">
            <Name>SAVEA</Name>
        </Value>
        <Value Row="196" Column="1" ColumnName="CustomerId">
            <Name>SAVEA</Name>
        </Value>
        <Value Row="219" Column="1" ColumnName="CustomerId">
            <Name>SAVEA</Name>
        </Value>
        <Value Row="242" Column="1" ColumnName="CustomerId">
            <Name>WHITC</Name>
        </Value>
        <Value Row="258" Column="1" ColumnName="CustomerId">
            <Name>WHITC</Name>
        </Value>
        <Value Row="274" Column="1" ColumnName="CustomerId">
            <Name>WHITC</Name>
        </Value>
        <Value Row="290" Column="1" ColumnName="CustomerId">
            <Name>WHITC</Name>
        </Value>
    </RowDefItems>
    <UserContext>
    <MachineLoginName>MaryM</MachineLoginName>
    <MachineName>.</MachineName>
    <FullName> </FullName>
    <UserId>UUvP4HYoeu</UserId>
    <ClientId>CgCfW9qi</ClientId>
    <LoginName>Mary@mycompany.com</LoginName>
    <LoginAuthTypeId>10</LoginAuthTypeId>
    <LoginDateUtc>05/03/2018 5:39:48</LoginDateUtc>
    <UserRoles>
        <Role>ClientAdmin</Role>
    </UserRoles>
</UserContext>
    <UserContextEncrypted>Encrypted only through interject api protocol, not direct connection</UserContextEncrypted>
    <XMLDataToSave></XMLDataToSave>
</RequestContext>'