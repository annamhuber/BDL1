SELECT Country, COUNT(Country) AS cnt
  FROM Customer
  GROUP BY Country
  ORDER BY COUNT(Country) DESC
;

SELECT
  InvoiceId,
  Amount AS MaxInvoice
  FROM (
        SELECT
              InvoiceId,
              SUM(UnitPrice * Quantity) AS Amount
          FROM InvoiceLine
          GROUP BY  InvoiceId
        ) x
  ORDER BY Amount DESC
;

SELECT
      COUNT(il.Quantity) AS "Times_Purchased",
      t.Trackid,
      t.Name,
      m.Name AS "Media_Type",
      m.MediaTypeId
  FROM Track t
       JOIN MediaType    m ON m.MediaTypeId = t.MediaTypeId
       JOIN InvoiceLine il ON il.TrackId = t.Trackid
  GROUP BY m.Name
  ORDER BY "Times_Purchased" DESC
;
