SELECT 
    users."name", 
    users.email, 
    roles.description AS role_description, 
    claims.description AS claim_description
FROM 
    users
JOIN 
    roles ON users.role_id = roles.id
JOIN 
    user_claims ON users.id = user_claims.user_id
JOIN 
    claims ON user_claims.claim_id = claims.id;