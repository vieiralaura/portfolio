SELECT c.*
	,v.version
    ,v.MailInd AS ind
    ,CASE WHEN v.MailInd = 1.0 THEN "1" ELSE "0" END AS email
    ,CASE WHEN s.spend IS NULL THEN 0 ELSE s.spend END AS spent
    ,CASE WHEN s.spend IS NOT NULL THEN 1 ELSE 0 END AS shopper
    ,CASE WHEN s.spend < 0 THEN "1" ELSE 0 END AS negative
    ,ips.profile_description AS profile
    ,iss.segment_description AS segment
FROM customers c
INNER JOIN versions v
	ON c.id = v.id
LEFT JOIN sales s
	ON c.id = s.id
LEFT JOIN info_profiles ips
	ON c.ProfileId = ips.ProfileID
LEFT JOIN info_segments iss
	ON c.SegmentID = iss.SegmentID
