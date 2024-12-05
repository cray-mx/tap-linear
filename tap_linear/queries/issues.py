issuesQuery = """
        query Issues($next: String, $replicationKeyValue: DateTimeOrDuration) {
						issues(
							first: 100
							after: $next
							filter: { updatedAt: {gt: $replicationKeyValue } }
						) {
							pageInfo {
								hasNextPage
								endCursor
							}
							nodes {
								id
								title
								url
								createdAt
								updatedAt
								canceledAt
								completedAt
								dueDate,
								priority
								priorityLabel
								description
								identifier
								creator {
									id
									name
									email
								}
								assignee {
									id
									name
									email
								}
								project {
									id
									name
								}
								team {
									id
									name
								}
								state {
									createdAt
									id
									name
									updatedAt
									position
								}
							}
						}
					}
        """
