SELECT d.*
	,ids.Department_description AS department
    ,ips.profile_description AS profile
    ,iss.segment_description AS segment
FROM depts d
LEFT JOIN info_departments ids
	ON d.DepartmentID = ids.DepartmentID
LEFT JOIN info_profiles ips
	ON d.ProfileId = ips.ProfileID
LEFT JOIN info_segments iss
	ON d.SegmentID = iss.SegmentID
